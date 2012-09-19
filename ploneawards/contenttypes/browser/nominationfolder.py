import random

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from tweet import tweeturl


class NominationFolderView(BrowserView):
    """Standalone view for a nomination folder.
    """

    index = ViewPageTemplateFile("templates/nominationfolder.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def rows(self):
        rows = []
        cells = []
        items = self.context.listFolderContents(
            contentFilter={'review_state': 'published'})
        queue = [x for x in items]
        while queue:
            nomination = random.choice(queue)
            queue.remove(nomination)
            cells.append(nomination)
            if len(cells) == 2:
                rows.append(cells)
                cells = []
        if cells:
            rows.append(cells)
        return rows

    def tweeturl(self, nomination):
        return tweeturl(nomination)
