from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets import PloneMessageFactory as _
try:
    from plone.app.portlets.browser import z3cformhelper
    P_A_PORTLETS_PRE_3 = True
except:
    P_A_PORTLETS_PRE_3 = False
from plone.app.portlets.portlets import base
from plone.app.event.portlets.portlet_calendar import Renderer as RendererBase
from plone.app.event.portlets.portlet_calendar import ICalendarPortlet
from plone.app.event.portlets.portlet_calendar import Assignment
if P_A_PORTLETS_PRE_3:
    from z3c.form import field


class Renderer(RendererBase):
    render = ViewPageTemplateFile('portlet_calendar.pt')


class AddForm(base.AddForm):
    if P_A_PORTLETS_PRE_3:
        fields = field.Fields(ICalendarPortlet)
    else:
        schema = ICalendarPortlet
    label = _(u"Add Calendar Portlet")
    description = _(u"This portlet displays events in a calendar.")

    def create(self, data):
        return Assignment(state=data.get('state', None),
                          search_base_uid=data.get('search_base_uid', None))


class EditForm(base.EditForm):
    if P_A_PORTLETS_PRE_3:
        fields = field.Fields(ICalendarPortlet)
    else:
        schema = ICalendarPortlet
    label = _(u"Edit Calendar Portlet")
    description = _(u"This portlet displays events in a calendar.")
