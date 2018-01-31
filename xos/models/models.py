from xos.exceptions import XOSValidationError

from models_decl import MCordSubscriberService_decl
from models_decl import MCordSubscriberInstance_decl




class MCordSubscriberService(MCordSubscriberService_decl):
    class Meta:
        proxy = True 


class MCordSubscriberInstance(MCordSubscriberInstance_decl):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        # NOTE someone is setting owner_id, so just override it for now
        try:
            mcord_service = MCordSubscriberService.objects.all()[0]
            self.owner_id = mcord_service.id
        except IndexError:
            raise XOSValidationError("Service MCORD cannot be found, please make sure that the model exists.")

        super(MCordSubscriberInstance, self).save(*args, **kwargs)
