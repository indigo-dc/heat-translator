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

import os

from translator.hot.syntax.hot_resource import HotResource


class HotResourceGroup(HotResource):

    def __init__(self, nodetemplate, name, resources, nb, csar_dir=None):
        super(HotResourceGroup, self).__init__(nodetemplate,
                                               name=name,
                                               type='OS::Heat::ResourceGroup',
                                               csar_dir=csar_dir)

        self.properties = {'resource_def': resources, 'count': nb}

    def extract_substack_templates(self, resources, base_filename,
                                   hot_template_version):
        # create a substack to embed the server
        # and its dependencies
        template, parameters, deps = self.create_substack_from_servers(
            self.properties['resource_def'], resources)
        self.depends_on = deps

        base_filename, ext = os.path.splitext(base_filename)

        filename = base_filename + "_" + self.name + ext
        self.properties['resource_def'] = {'type': filename}
        if parameters:
            self.properties['resource_def']['properties'] = parameters

        nested_templates = {
            filename: template.output_to_yaml(True, hot_template_version)
        }

        return nested_templates, template.resources

    def embed_substack_templates(self, resources, hot_template_version):
        # create a substack to embed the server
        # and its dependencies
        template, parameters, deps = self.create_substack_from_servers(
            self.properties['resource_def'], resources)
        self.depends_on = deps

        self.properties['resource_def'] = {'type': 'OS::Heat::Stack'}
        self.properties['resource_def']['properties'] = {
            'template': template.output_to_yaml(True, hot_template_version)
        }

        if parameters:
            self.properties['resource_def']['properties']['parameters'] = \
                parameters

        return template.resources

    def handle_properties(self, resources):
        pass
