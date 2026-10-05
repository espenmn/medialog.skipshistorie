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
from pypdf import PdfWriter


import os
#import tempfile
#import zipfile



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
            url = item.absolute_url()

            if item.portal_type == "Skip":
                url = "{}/skip-view".format(url)

            urls.append(url)


        # Convert each URL separately
        writer = PdfWriter()

        for url in urls:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp_pdf = tmp.name

            try:
                pdfkit.from_url(url, tmp_pdf)

                # Add this PDF to the final document
                from pypdf import PdfReader
                reader = PdfReader(tmp_pdf)

                for page in reader.pages:
                    writer.add_page(page)

            finally:
                if os.path.exists(tmp_pdf):
                    os.unlink(tmp_pdf)


        with open("out.pdf", "wb") as f:
            writer.write(f)
                    
      
        import io

        pdf_data = io.BytesIO()
        writer.write(pdf_data)

        pdf_data.seek(0)

        self.request.response.setHeader("Content-Type", "application/pdf")
        self.request.response.setHeader(
            "Content-Disposition",
            'inline; filename="out.pdf"'
        )

        return pdf_data.getvalue()

