from PyQt5 import QtCore, QtGui, QtWidgets
import popplerqt5

inter_page_space = 10


class PdfView(QtWidgets.QGraphicsView):

    def __init__(self, parent=None):
        super(PdfView, self).__init__(parent)

        self.dpi_x = QtWidgets.QApplication.desktop().physicalDpiX()
        self.dpi_y = QtWidgets.QApplication.desktop().physicalDpiY()

        self.zoom_factor = 1
        self.page_number = 0

        self.vertical_position_timer = QtCore.QTimer()
        self.vertical_position_timer.setSingleShot(True)
        self.vertical_position_timer.setInterval(0)
        self.vertical_position_timer.timeout.connect(
            self.on_vertical_position_changed)

        self.page_scene = QtWidgets.QGraphicsScene()
        self.setScene(self.page_scene)

    @property
    def scale_factor_x(self):
        return self.zoom_factor * self.dpi_x / 72.0

    @property
    def scale_factor_y(self):
        return self.zoom_factor * self.dpi_y / 72.0

    def load_document(self, filename):
        """
        Loads the specified document using Poppler, sets up each page in the
        QGraphicsScene.
        """
        print("loading document")
        self.filename = filename

        self.doc = popplerqt5.Poppler.Document.load(filename)
        self.doc.setRenderHint(popplerqt5.Poppler.Document.Antialiasing)
        self.doc.setRenderHint(popplerqt5.Poppler.Document.TextAntialiasing)

        page_count = self.doc.numPages()
        self.pages = []
        self.page_top_positions = []
        self.pages_loaded = []
        max_page_width = 0
        for i in range(page_count):
            page = self.doc.page(i)
            self.pages.append(page)
            if i == 0:
                self.page_top_positions.append(inter_page_space/2)
            else:
                old_size = page.pageSizeF()
                top = (self.page_top_positions[-1] +
                       old_size.height() +
                       inter_page_space)
                self.page_top_positions.append(top)

                max_page_width = max(old_size.width(), max_page_width)

            page_rect = self.map_from_page(
                i, QtCore.QRectF(QtCore.QPointF(0, 0), page.pageSizeF()))

            # black border
            rect = self.page_scene.addRect(
                page_rect, QtGui.QPen(QtGui.QBrush(QtCore.Qt.black), 1))
            rect.setZValue(1)
            rect.setData(0, i)

            # white background
            self.page_scene.addRect(
                page_rect, QtGui.QPen(), QtGui.QBrush(QtCore.Qt.white))

            self.pages_loaded.append(False)

        self.page_top_positions.append(
            (self.page_top_positions[-1] +
                self.pages[-1].pageSizeF().height() +
                inter_page_space/2))
        self.page_scene.setSceneRect(
            0, 0,
            (max_page_width+inter_page_space)*self.scale_factor_x+2,
            self.page_top_positions[-1]*self.scale_factor_y+2)

        self.verticalScrollBar().valueChanged.connect(
            self.on_vertical_position_changed)
        self.set_page(0)

    def close(self):
        del self.pages[:]
        self.page_scene.clear()

    def load_page(self, page_number):
        print("loading page {}".format(page_number))
        res_x = self.dpi_x * self.zoom_factor
        res_y = self.dpi_y * self.zoom_factor
        image = self.pages[page_number].renderToImage(res_x, res_y)

        if image.isNull():
            print("image is null")
            return

        page_item = self.page_scene.addPixmap(QtGui.QPixmap.fromImage(image))
        m = self.map_from_page(page_number, QtCore.QPointF(0, 0))
        print(m)
        page_item.setOffset(self.map_from_page(
            page_number, QtCore.QPointF(0, 0)))
        page_item.setData(1, page_number)

        self.pages_loaded[page_number] = True

    def load_visible_pages(self, page_number_start, page_number_end):
        page_count = self.doc.numPages()
        for i in range(max(0, page_number_start), page_number_end):
            if i >= page_count:
                break
            if not self.pages_loaded[i]:
                self.load_page(i)

    def clear_pages(self):
        page_count = self.doc.numPages()
        items = self.page_scene.items()
        for i in range(len(items)):
            page_number = items[i].data(1)
            if page_number is None:
                continue
            if page_number >= 0 and page_number < page_count:
                self.page_scene.removeItem(items[i])
                del items[i]
                self.pages_loaded[page_number] = False

    def clear_nonvisible_pages(self, page_number_start, page_number_end):
        page_count = self.doc.numPages()
        buf = 25
        items = self.page_scene.items()
        for i in range(len(items)):
            page_number = items[i].data(1)
            if page_number is None:
                continue
            if ((page_number >= 1 and page_number < page_number_start - buf) or
                    (page_number > page_number_end + buf and
                        page_number < page_count)):
                self.page_scene.removeItem(items[i])
                del items[i]
                self.pages_loaded[page_number] = False

    def set_page(self, page_number, keep_pos=False):
        print("set page {}".format(page_number))
        page_number_start = page_number
        page_number_end = page_number
        max_top_position = (self.page_top_positions[page_number_start] +
                            self.viewport().height() / self.scale_factor_y)
        page_count = self.doc.numPages()
        for i in range(page_number_start, page_count):
            if self.page_top_positions[i] > max_top_position:
                break
            page_number_end += 1

        # TODO: handle last page

        if page_number_start < 0:
            page_number_start = 0

        self.load_visible_pages(page_number_start, page_number_end)
        self.clear_nonvisible_pages(page_number_start, page_number_end)

        if not keep_pos:
            return

        # vbar = self.verticalScrollBar()
        # self.verticalScrollBar().valueChanged.connect(
        #     self.on_vertical_position_changed)

    def map_from_page(self, page_number, page_param):
        """
        Maps a point or rect in page coordinates to scene coordinates.

        Parameters
        ----------
        page_number : int
            The page number to perform the mapping for.
        page_param : QPointF or QRectF
            The point or rect in page coordinates.

        Returns
        -------
        scene_param : QPointF or QRectF
            The point or rect in scene coordinates.
        """
        x = (page_param.x() + inter_page_space/2) * self.scale_factor_x
        y = ((page_param.y() + self.page_top_positions[page_number]) *
             self.scale_factor_y)

        if type(page_param) == QtCore.QPointF:
            return QtCore.QPointF(x, y)
        else:
            w = page_param.width() * self.scale_factor_x
            h = page_param.height() * self.scale_factor_y
            return QtCore.QRectF(x, y, w, h)

    def map_to_page(self, page_number, scene_param):
        """
        Maps a point or rect in scene coordinates to page coordinates.

        Parameters
        ----------
        page_number : int
            The page number to perform the mapping for.
        scene_param : QPointF or QRectF
            The point or rect in scene coordinates.

        Returns
        -------
        page_param : QPointF or QRectF
            The point or rect in page coordinates.
        """
        x = scene_param.x() / self.scale_factor_x - inter_page_space/2
        y = (scene_param.y() / self.scale_factor_y -
             self.page_top_positions[page_number])

        if type(scene_param) == QtCore.QPointF:
            return QtCore.QPointF(x, y)
        else:
            w = scene_param.width() / self.scale_factor_x
            h = scene_param.height() / self.scale_factor_y
            return QtCore.QRectF(x, y, w, h)

    def map_to_current_page(self, scene_pos):
        """
        Maps a point in scene coordinates to the current page's coordinates.
        The current page is the one visible at the input `scene_pos`.

        Parameters
        ----------
        scene_pos : QPointF
            The point in scene coordinates to convert.

        Returns
        -------
        page_pos : QPointF
            The point in page coordinates.
        """
        page_number = self.page_number_at_position(scene_pos)
        return self.map_to_page(page_number, scene_pos)

    def page_number_with_position(self):
        """
        Gets the value containing the number of the current page together with
        the fraction of this page on which the top of the currently visible
        area is located.
        """
        pass

    def on_vertical_position_changed(self, value=None):
        if value is not None:
            if self.vertical_position_timer.isActive():
                self.vertical_position_timer.stop()
            self.vertical_position_timer.start()
        else:
            vbar = self.verticalScrollBar()
            vbarval = ((vbar.value() + inter_page_space / 2) /
                       self.scale_factor_y)
            page_num = 0
            page_count = self.doc.numPages()
            for i in range(page_num, page_count):
                if self.page_top_positions[i] > vbarval:
                    break
                page_num += 1
            page_num -= 1
            if page_num < 0:
                page_num = 0

            if self.page_number != page_num:
                self.set_page(page_num, False)
                self.page_number = page_num
