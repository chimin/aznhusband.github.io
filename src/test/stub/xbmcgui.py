class Dialog:

    preferredSources = ['1024', '720', '480', '320']

    def select(self, title, items):
        if title == '33034':
            for preferredSource in self.preferredSources:
                for index, item in enumerate(items):
                    if preferredSource in item:
                        return index
            return 0
        else:
            raise


class WindowDialog:
    pass


class WindowXMLDialog:
    pass


class ListItem:

    def __init__(self, label, iconImage):
        print "ListItem " + str(label) + " " + str(iconImage)
        pass

    def addContextMenuItems(self, menu, replaceItems):
        print "ListItem.addContextMenuItems " + str(menu)
        pass
