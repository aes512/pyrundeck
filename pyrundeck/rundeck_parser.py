# Copyright (c) 2015, National Documentation Centre (EKT, www.ekt.gr)
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
import logging

from pyrundeck.xml2native import ParserEngine

__author__ = "Panagiotis Koutsourakis <kutsurak@ekt.gr>"


class RundeckParser(object):
    """This class contains the parsing tables for various rundeck elements.

    Each parse table describes a specific tag. See
    :py:class:`pyrundeck.xml2native.ParserEngine` for more details.

    """
    def __init__(self, log_level=logging.INFO):
        self.error_parse_table = {
            'tag': 'error',
            'type': 'composite',
            'all': [{'tag': 'message', 'type': 'text'}]
        }

        self.start_date_parse_table = {
            'tag': 'date-started',
            'type': 'attribute text',
            'text tag': 'time'
        }

        self.date_ended_parse_table = {
            'tag': 'date-ended',
            'type': 'attribute text',
            'text tag': 'time'
        }

        self.node_parse_table = {
            'tag': 'node',
            'type': 'attribute'
        }

        self.successful_nodes_parse_table = {
            'tag': 'successfulNodes',
            'type': 'list',
            'element parse table': self.node_parse_table,
            'skip count': True,
        }

        self.failed_nodes_parse_table = {
            'tag': 'failedNodes',
            'type': 'list',
            'element parse table': self.node_parse_table,
            'skip count': True,
        }

        self.option_parse_table = {
            'tag': 'option',
            'type': 'composite',
            'any': [
                {'tag': 'description', 'type': 'text'}
            ]
        }

        self.options_parse_table = {
            'tag': 'options',
            'type': 'list',
            'element parse table': self.option_parse_table,
            'skip count': True
        }

        self.job_parse_table = {
            'tag': 'job',
            'type': 'composite',
            'all': [
                {'tag': 'id', 'type': 'text'},
                {'tag': 'name', 'type': 'text'},
                {'tag': 'project', 'type': 'text'},
            ],
            'any': [
                {'tag': 'group', 'type': 'text'},
                {'tag': 'description', 'type': 'text'},
                {'tag': 'url', 'type': 'text'},
                {'tag': 'group', 'type': 'text'},
                self.options_parse_table
            ]
        }

        self.jobs_parse_table = {
            'tag': 'jobs',
            'type': 'list',
            'element parse table': self.job_parse_table
        }

        self.execution_parse_table = {
            'tag': 'execution',
            'type': 'composite',
            'all': [
                {'tag': 'user', 'type': 'text'},
                self.start_date_parse_table,
                {'tag': 'description', 'type': 'text'}
            ],
            'any': [
                self.job_parse_table,
                {'tag': 'argstring', 'type': 'text'},
                {'tag': 'serverUUID', 'type': 'text'},
                {'tag': 'abortedby', 'type': 'text'},
                self.date_ended_parse_table,
                self.successful_nodes_parse_table,
                self.failed_nodes_parse_table
            ]
        }

        self.executions_parse_table = {
            'tag': 'executions',
            'type': 'list',
            'element parse table': self.execution_parse_table
        }

        self.succeeded_job_list = {
            'tag': 'succeeded',
            'type': 'list',
            'element parse table': self.job_parse_table,

        }

        self.failed_job_list = {
            'tag': 'failed',
            'type': 'list',
            'element parse table': self.job_parse_table,

        }

        self.skipped_job_list = {
            'tag': 'skipped',
            'type': 'list',
            'element parse table': self.job_parse_table,

        }

        self.success_parse_table = {
            'tag': 'success',
            'type': 'composite',
            'all': [
                {'tag': 'message', 'type': 'text'}
            ]
        }

        self.timestamp_parse_table = {
            'tag': 'timestamp',
            'type': 'composite',
            'all': [{'tag': 'datetime', 'type': 'text'}]
        }

        self.rundeck_info_parse_table = {
            'tag': 'rundeck',
            'type': 'composite',
            'all': [
                {'tag': 'version', 'type': 'text'},
                {'tag': 'build', 'type': 'text'},
                {'tag': 'node', 'type': 'text'},
                {'tag': 'base', 'type': 'text'},
                {'tag': 'apiversion', 'type': 'text'},
                {'tag': 'serverUUID', 'type': 'text'},
            ]
        }

        self.os_parse_table = {
            'tag': 'os',
            'type': 'composite',
            'all': [
                {'tag': 'arch', 'type': 'text'},
                {'tag': 'name', 'type': 'text'},
                {'tag': 'version', 'type': 'text'},
            ]
        }

        self.jvm_parse_table = {
            'tag': 'jvm',
            'type': 'composite',
            'all': [
                {'tag': 'name', 'type': 'text'},
                {'tag': 'vendor', 'type': 'text'},
                {'tag': 'version', 'type': 'text'},
                {'tag': 'implementationVersion', 'type': 'text'},
            ]
        }

        self.uptime_parse_table = {
            'tag': 'uptime',
            'type': 'composite',
            'all': [
                {
                    'tag': 'since',
                    'type': 'composite',
                    'all': [{'tag': 'datetime', 'type': 'text'}]
                }
            ]
        }

        self.cpu_parse_table = {
            'tag': 'cpu',
            'type': 'composite',
            'all': [
                {
                    'tag': 'loadAverage',
                    'type': 'attribute text',
                    'text tag': 'load'
                },
                {'tag': 'processors', 'type': 'text'}
            ]
        }

        self.memory_parse_table = {
            'tag': 'memory',
            'type': 'composite',
            'all': [
                {'tag': 'max', 'type': 'text'},
                {'tag': 'free', 'type': 'text'},
                {'tag': 'total', 'type': 'text'}
            ]
        }

        self.scheduler_parse_table = {
            'tag': 'scheduler',
            'type': 'composite',
            'all': [
                {'tag': 'running', 'type': 'text'},
            ]
        }

        self.threads_parse_table = {
            'tag': 'threads',
            'type': 'composite',
            'all': [
                {'tag': 'active', 'type': 'text'},
            ]
        }

        self.stats_parse_table = {
            'tag': 'stats',
            'type': 'composite',
            'all': [
                self.uptime_parse_table,
                self.cpu_parse_table,
                self.memory_parse_table,
                self.scheduler_parse_table,
                self.threads_parse_table
            ]
        }

        self.system_info_parse_table = {
            'tag': 'system',
            'type': 'composite',
            'all': [
                self.timestamp_parse_table,
                self.rundeck_info_parse_table,
                self.os_parse_table,
                self.jvm_parse_table,
                self.stats_parse_table,
                {'tag': 'metrics', 'type': 'attribute'},
                {'tag': 'threadDump', 'type': 'attribute'},
            ]
        }

        self.deleteJobResult_parse_table = {
            'tag': 'deleteJobResult',
            'type': 'alternatives',
            'parse tables': [
                {
                    'type': 'composite',
                    'all': [
                        {
                            'tag': 'message',
                            'type': 'text'
                        }
                    ]
                },
                {
                    'type': 'composite',
                    'all': [
                        {
                            'tag': 'error',
                            'type': 'text'
                        }
                    ]
                }
            ]
        }

        self.delete_jobs_parse_table = {
            'tag': 'deleteJobs',
            'type': 'composite',
            'any': [
                {
                    'tag': 'succeeded',
                    'type': 'list',
                    'element parse table': self.deleteJobResult_parse_table
                },
                {
                    'tag': 'failed',
                    'type': 'list',
                    'element parse table': self.deleteJobResult_parse_table
                }
            ]
        }

        self.result_parse_table = {
            'tag': 'result',
            'type': 'alternatives',
            'parse tables': [
                {'type': 'composite', 'all': [self.jobs_parse_table]},
                {'type': 'composite', 'all': [self.error_parse_table]},
                {'type': 'composite', 'all': [self.executions_parse_table]},
                {
                    'type': 'composite',
                    'all': [
                        self.succeeded_job_list,
                        self.failed_job_list,
                        self.skipped_job_list,
                    ],
                },
                {
                    'type': 'composite',
                    'all': [
                        self.success_parse_table,
                        self.system_info_parse_table
                    ]
                },
                {
                    'type': 'composite',
                    'all': [self.delete_jobs_parse_table]
                },
            ],
        }

        self.simple_command_parse_table = {
            'tag': 'command',
            'type': 'composite',
            'all': [
                {'tag': 'exec', 'type': 'text'}
            ]
        }

        self.script_command_parse_table = {
            'tag': 'command',
            'type': 'composite',
            'any': [
                {'tag': 'script', 'type': 'text'},
                {'tag': 'scriptargs', 'type': 'text'},
                {'tag': 'scripturl', 'type': 'text'},
                {
                    'tag': 'errorhandler',
                    'type': 'composite',
                    'any': [
                        {'tag': 'exec', 'type': 'text'},
                        {'tag': 'scriptargs', 'type': 'text'},
                        {'tag': 'scripturl', 'type': 'text'},
                    ]
                }
            ]
        }

        self.jobref_command_parse_table = {
            'tag': 'command',
            'type': 'composite',
            'all': [
                {
                    'tag': 'jobref',
                    'type': 'composite',
                    'any': [
                        {'tag': 'arg', 'type': 'attribute'}
                    ],
                },
            ]
        }

        self.joblist_job_parse_table = {
            'tag': 'job',
            'type': 'composite',
            'all': [
                {'tag': 'id', 'type': 'text'},
                {'tag': 'loglevel', 'type': 'text'},
                {
                    'tag': 'sequence',
                    'type': 'composite',
                    'all': [
                        {
                            'tag': 'command',
                            'type': 'alternatives',
                            'parse tables': [
                                self.simple_command_parse_table,
                                self.script_command_parse_table,
                                self.jobref_command_parse_table
                            ]
                        }
                    ]
                },
                {'tag': 'name', 'type': 'text'},
                {'tag': 'uuid', 'type': 'text'},
                {
                    'tag': 'context',
                    'type': 'composite',
                    'all': [
                        {'tag': 'project', 'type': 'text'}
                    ],
                    'any': [
                        self.options_parse_table,
                    ],
                }
            ],
            'any': [
                {'tag': 'description', 'type': 'text'},
                {'tag': 'group', 'type': 'text'},
                {
                    'tag': 'dispatch',
                    'type': 'composite',
                    'any': [
                        {'tag': 'threadcount', 'type': 'text'},
                        {'tag': 'keepgoing', 'type': 'text'},
                        {'tag': 'excludePrecedence', 'type': 'text'},
                        {'tag': 'rankOrder', 'type': 'text'},
                    ]
                },
                {
                    'tag': 'nodefilters',
                    'type': 'list',
                    'element parse table': {
                        'tag': 'filter',
                        'type': 'text'
                    },
                    'skip count': True
                },
                {'tag': 'multipleExecutions', 'type': 'text'},
                {
                    'tag': 'schedule',
                    'type': 'composite',
                    'any': [
                        {'tag': 'time', 'type': 'attribute'},
                        {'tag': 'weekday', 'type': 'attribute'},
                        {'tag': 'month', 'type': 'attribute'},
                        {'tag': 'year', 'type': 'attribute'},
                    ]
                },
                {
                    'tag': 'notification',
                    'type': 'composite',
                    'any': [
                        {
                            'tag': 'onfailure',
                            'type': 'composite',
                            'any': [{'tag': 'email', 'type': 'attribute'}]
                        },
                        {
                            'tag': 'onsuccess',
                            'type': 'composite',
                            'any': [{'tag': 'email', 'type': 'attribute'}]
                        },

                    ]
                }
            ]
        }

        self.joblist_parse_table = {
            'tag': 'joblist',
            'type': 'list',
            'element parse table': self.joblist_job_parse_table,
            'skip count': True
        }

        self.start_symbol = {
            'type': 'alternatives',
            'parse tables': [
                self.result_parse_table,
                self.joblist_parse_table
            ]
        }

        self.engine = ParserEngine(log_level=log_level)

    def parse(self, xml_tree, cb_type, parse_table):
        """This method is the external interface to the ParserEngine class.

        The parse table for each element must contain a key named
        ``'type'`` that should contain the type of the parse function
        that should be called to parse this tag. This is the
        ``cb_type`` argument of the parse method.

        """
        # Create a parser engine.

        # Find which call back we need to call...
        cb = self.engine.callbacks[cb_type]
        # ... and call it
        return cb(xml_tree, parse_table)

# The entry point for this module
_parser = RundeckParser()


def parse(xml_tree, cb_type='alternatives',
          parse_table=_parser.start_symbol):
    """Main entry point to the parser"""
    return _parser.parse(xml_tree, cb_type, parse_table)
