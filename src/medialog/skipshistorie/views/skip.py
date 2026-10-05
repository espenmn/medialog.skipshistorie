# -*- coding: utf-8 -*-

#from medialog.skipshistorie import _
from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from medialog.skipshistorie import _
from zope.interface import implementer
from zope.interface import Interface
from jinja2 import Environment
from jinja2 import FileSystemLoader
from pdfkit import from_string
import pdfkit



import os
import tempfile
import zipfile



class ISkipView(Interface):
    """ Marker Interface for IBoatView"""





@implementer(ISkipView)
class SkipView(BrowserView):
    """ Converter view forSkip.
    """
    template = ViewPageTemplateFile('skip.pt')


    def __init__(self, context, request, expr, engine):
        super().__init__(context, request)


    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
            'convertFootnotes',
            'removeCrapFromHeadings',
            'fixHierarchies',
        )

        return self.template(self.context, **data)

InitializeClass(SkipView)



class toPDF(BrowserView):
    """ Converter view forSkip.
    """


    def __call__(self):
        """Returns the pdf file,
        """
        request = self.request
        context = self.context
        portal_type = context.portal_type
        pdfTitle = self.context.title + '.pdf'
        
        if portal_type in ["Folder", "Collection"]:
            items = self.context.listFolderContents()
        else:
            items = [self.context]

        urls = []

        for item in items:
            if item.portal_type in ["Skip", "skip"]:
                url = "{}/skip-view".format(item.absolute_url())

                urls.append(url)
   

        

        with tempfile.TemporaryDirectory() as temp_dir:

                zip_path = os.path.join(temp_dir, "{}.zip".format(pdfTitle))

                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:

                    for index, url in enumerate(urls, 1):

                        pdf_path = os.path.join(
                            temp_dir,
                            "document-{}.pdf".format(index)
                        )

                        # Create PDF
                        pdfkit.from_url(url, pdf_path)

                        # Add PDF to ZIP
                        zip_file.write(
                            pdf_path,
                            arcname="document-{}.pdf".format(index)
                        )

                # Read completed ZIP before TemporaryDirectory disappears
                with open(zip_path, "rb") as f:
                    zip_data = f.read()


        R = self.request.RESPONSE

        R.setHeader("Content-Type", "application/zip")
        R.setHeader(
                "Content-Disposition",
                'attachment; filename="{}.zip"'.format(pdfTitle)
        )
        R.setHeader("Content-Length", len(zip_data))

        return zip_data


