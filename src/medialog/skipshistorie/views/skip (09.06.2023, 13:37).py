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
        context = self.context
        #myHtml = '{{context/vessel|None}}'
        #template = Template('jinja2_template_string')

        # Render HTML Template String
        #html_template_string = template.render()
        #css = '++theme++dutchestheme/less/blue/theme.css'

        url = "{}/skip-view".format( self.context.absolute_url() )

        #myFile = pdfkit.from_string(html_template_string,'out.pdf')

        myFile = pdfkit.from_url(url,'out.pdf')
        #http://localhost:skipshistorie/arendal/arn758ahauge/arn75819480100000-tora
        #import pdb; pdb.set_trace()

        #url = self.context.absolute_url()
        #myFile = pdfkit.from_url(url,'out.pdf')


        return myFile

        #pdfkit.from_url('https://www.google.co.in/','shaurya.pdf')
