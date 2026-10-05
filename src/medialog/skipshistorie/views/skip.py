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
            # url = item.absolute_url()

            if item.portal_type in ["Skip", "skip"]:
                url = "{}/skip-view".format(url)

            urls.append(url)
   

        ## Need to use 'tempfile for this in case two people downloads at the same time'
        pdfFile = pdfkit.from_url(urls, "out.pdf")
        R = self.request.RESPONSE

        #Probably add all the files to a folder and zip it instead
        #file_path = os.path.join(os.getcwd(), 'out.pdf')

        with open('out.pdf', 'rb') as f:
            pdf_data = f.read()

        R.setHeader('Content-Type', 'application/pdf')
        R.setHeader('Content-Disposition', 'inline; filename=out.pdf')
        R.setHeader("Content-Disposition", "attachment; filename=%s.pdf" % pdfTitle)
        R.setHeader('Content-Length', len(pdf_data))

        return pdf_data
        #return pdfFile


