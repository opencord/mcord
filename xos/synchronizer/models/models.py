# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
