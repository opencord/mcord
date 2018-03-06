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
        # if we don't have a name, use the IMSI number has a name
        if not self.name:
            self.name = self.imsi_number

        # prevent IMSI duplicate
        try:
            instance_with_same_imsi = MCordSubscriberInstance.objects.get(imsi_number=self.imsi_number)

            if (not self.pk and instance_with_same_imsi) or (self.pk and self.pk != instance_with_same_imsi.pk):
                raise XOSValidationError("An MCORDSubscriber with imsi_number '%s' already exists" % self.imsi_number)
        except self.DoesNotExist:
            pass

        if self.is_new and not self.created_by:
            # NOTE if created_by is null it has been created by XOS
            self.created_by = "XOS"

        self.backend_code = 0
        self.backend_status = "In Progress"

        super(MCordSubscriberInstance, self).save(*args, **kwargs)
