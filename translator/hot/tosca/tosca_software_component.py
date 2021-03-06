#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from toscaparser.utils.gettextutils import _
from translator.hot.syntax.hot_resource import HotResource


log = logging.getLogger('heat-translator')


# Name used to dynamically load appropriate map class.
TARGET_CLASS_NAME = 'ToscaSoftwareComponent'


class ToscaSoftwareComponent(HotResource):
    '''Translate TOSCA node type tosca.nodes.SoftwareComponent.'''

    toscatype = 'tosca.nodes.SoftwareComponent'

    def __init__(self, nodetemplate, csar_dir=None):
        super(ToscaSoftwareComponent, self).__init__(nodetemplate,
                                                     csar_dir=csar_dir)
        pass

    def handle_properties(self):
        pass

    def get_hot_attribute(self, attribute, args):
        attr = {}
        # Convert from a TOSCA attribute for a nodetemplate to a HOT
        # attribute for the matching resource.  Unless there is additional
        # runtime support, this should be a one to one mapping.

        # Note: We treat private and public IP  addresses equally, but
        # this will change in the future when TOSCA starts to support
        # multiple private/public IP addresses.
        log.debug(_('Converting TOSCA attribute for a nodetemplate to a HOT \
                  attribute.'))
        if attribute == 'private_address' or \
           attribute == 'public_address':
                attr['get_attr'] = [self.name, 'networks', 'private', 0]

        return attr
