import sys
from crudbase import *

class sliderbase(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

    def reset_children(self, target):
        children = target.children()
        if children == None:
            return

        for child in children:
            if "PyQt4" not in str(child.__class__):
                if hasattr(child, "reset_stack"):
                    child.reset_stack()

    def slider_setup(self, views, offset, widget):
        if views is None or offset is None or widget is None:
            return

        self.stacked_views = views
        self.stacked_offset = offset
        self.stacked_widget = widget
        self.signal_mapper = QtCore.QSignalMapper(self)

        for i, view in enumerate(self.stacked_views):
            self.stacked_widget.addWidget(view[0])
            self.signal_mapper.setMapping(view[1], i)
            view[1].clicked.connect(self.signal_mapper.map)

        self.signal_mapper.mapped.connect(self.show_stack_section)

    def show_stack_section(self, view_select):
        if self.stacked_widget is None:
            return

        self.reset_children(self.stacked_widget)
        self.stacked_widget.setCurrentIndex(view_select + self.stacked_offset)

    def reset_stack(self):
        if self.stacked_widget is None:
            return

        self.stacked_widget.setCurrentIndex(0)

