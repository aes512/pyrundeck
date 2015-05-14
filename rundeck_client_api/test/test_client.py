# Copyright (c) 2007-2015, National Documentation Centre (EKT, www.ekt.gr)
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

#     Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.

#     Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.

#     Neither the name of the National Documentation Centre nor the
#     names of its contributors may be used to endorse or promote
#     products derived from this software without specific prior written
#     permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__ = "Panagiotis Koutsourakis <kutsurak@ekt.gr>"
import requests
from rundeck_client_api import config
import nose.tools as nt

class TestRundeckClientAPIFunctional:
    def setup(self):
        with open(config.rundeck_token_file) as fl:
            token = fl.readline().strip()
            root_url = 'https://rundeck.ekt.gr'
            self.client = RundeckApiClient(token, root_url)

    def functional_client_test(self):
        # Find what endpoints are available
        endpoints = self.client.endpoints
        nt.assert_is_not_none(endpoints)

        # Find out what jobs are available
        nt.assert_is_not_none(endpoints.get('jobs'))
        status, data = self.client.perform_request('jobs')

        # TODO fill the assertions
