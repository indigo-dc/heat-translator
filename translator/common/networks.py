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

try:
    import neutronclient.v2_0.client
    client_available = True
except ImportError:
    client_available = False
    pass

log = logging.getLogger('heat-translator')

SESSION = None

PUBLIC_NETWORK = None

PRIVATE_NETWORK = None


def _init():
    global PUBLIC_NETWORK, PRIVATE_NETWORK

    if PUBLIC_NETWORK and PRIVATE_NETWORK:
        return

    if SESSION is not None and client_available:
        try:
            client = neutronclient.v2_0.client.Client(session=SESSION)
        except Exception as e:
            # Handles any exception coming from openstack
            log.warn(_('Choosing predefined networks since received '
                       'Openstack Exception: %s') % str(e))
        else:
            networks = client.list_networks()['networks']
            for network in networks:
                network_name = network["name"].encode('ascii', 'ignore')
                if network['shared'] and not PUBLIC_NETWORK:
                    PUBLIC_NETWORK = network_name
                if not network['shared'] and not PRIVATE_NETWORK:
                    PRIVATE_NETWORK = network_name

    if PRIVATE_NETWORK and not PUBLIC_NETWORK:
        PUBLIC_NETWORK = PRIVATE_NETWORK

    if PUBLIC_NETWORK and not PRIVATE_NETWORK:
        PRIVATE_NETWORK = PUBLIC_NETWORK

    if not PRIVATE_NETWORK and not PUBLIC_NETWORK:
        PRIVATE_NETWORK = 'private'
        PUBLIC_NETWORK = 'public'


def get_public_network():
    _init()
    return PUBLIC_NETWORK


def get_private_network():
    _init()
    return PRIVATE_NETWORK