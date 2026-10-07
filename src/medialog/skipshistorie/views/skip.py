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
        items = 0
        
        if portal_type in ["Folder", "Collection"]:
            items = self.context.listFolderContents()
        else:
            items = [self.context]
        
        R = self.request.RESPONSE

        if len(items) > 1:
            with tempfile.TemporaryDirectory() as temp_dir:
                zip_path = os.path.join(temp_dir, "{}.zip".format(pdfTitle))
                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:                    
                    for item in items:
                        if item.portal_type in ["Skip", "skip"]:
                            url = "{}/skip-view".format(item.absolute_url())
                            tittel = item.id
                            
                            # import pdb; pdb.set_trace()
                    
                            pdf_path = os.path.join(
                                temp_dir,
                                "{}.pdf".format(tittel)
                            )

                            # Create PDF
                            pdfkit.from_url(url, pdf_path)

                            # Add PDF to ZIP
                            zip_file.write(
                                pdf_path,
                                arcname="{}.pdf".format(tittel)
                            )

                # Read completed ZIP before TemporaryDirectory disappears
                with open(zip_path, "rb") as f:
                    zip_data = f.read()


        
            R.setHeader("Content-Type", "application/zip")
            R.setHeader(
                    "Content-Disposition",
                    'attachment; filename="{}.zip"'.format(pdfTitle)
            )
            R.setHeader("Content-Length", len(zip_data))

            return zip_data


        if len(items) == 1:
            pdfFile = pdfkit.from_url(items[0], "out.pdf")
            R = self.request.RESPONSE

            with open('out.pdf', 'rb') as f:
                pdf_data = f.read()

            R.setHeader('Content-Type', 'application/pdf')
            R.setHeader('Content-Disposition', 'inline; filename=out.pdf')
            R.setHeader("Content-Disposition", "attachment; filename=%s.pdf" % pdfTitle)
            R.setHeader('Content-Length', len(pdf_data))

            return pdf_data
        
        return "No ships found"
        