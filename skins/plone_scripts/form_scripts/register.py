## Script (Python) "register"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=password='password', confirm='confirm'
##title=Register a User
##
REQUEST=context.REQUEST

errors=context.portal_form_validateion.validate(context, 'validate_registration')
if errors:
    return context.join_form( context, REQUEST)

portal_registration=context.portal_registration
portal_properties=context.portal_properties

password=REQUEST.get('password') or portal_registration.generatePassword()
portal_registration.addMember(REQUEST['username'], password, properties=REQUEST)
if portal_properties.validate_email or REQUEST.get('mail_me', 0):
    portal_registration.registeredNotify(REQUEST['username'])

return context.registered( context, REQUEST )
