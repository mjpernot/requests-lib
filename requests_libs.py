# Classification (U)

"""Program:  requests_libs.py

    Description:  A library program that contains a number of modules for
        general Requests use.

    Functions:
        del_cmd
        get_query
        put_cmd

"""

# Libraries and Global Variables

# Standard

# Third-party
import requests
import json

# Local
import version

# Version
__version__ = version.__version__


def del_cmd(host, port, cmd, **kwargs):

    """Function:  del_cmd

    Description:  Create and execute a DELETE command.

    Arguments:
        (input) host -> Hostname
        (input) port -> Port to query on.
        (input) cmd -> Delete command.
        (input) **kwargs:
            None
        (output) Return status output of the command.

    """

    return requests.delete("http://" + host + ":" + str(port) + cmd).json()


def get_query(host, port, query, fmt="text", **kwargs):

    """Function:  get_query

    Description:  Create and execute a GET command.

    Arguments:
        (input) host -> Hostname
        (input) port -> Port to query on.
        (input) query -> Query statement.
        (input) fmt { json | text } -> Return format.
        (input) **kwargs:
            None
        (output) Return results of query.

    """

    if fmt == "json":
        return requests.get("http://" + host + ":" + str(port) + query).json()

    # Assume text format.
    else:
        return requests.get("http://" + host + ":" + str(port) + query).text


def put_cmd(host, port, cmd, data_dict=None, **kwargs):

    """Function:  put_cmd

    Description:  Create and execute a PUT command.

    Arguments:
        (input) host -> Hostname
        (input) port -> Port to query on.
        (input) cmd -> Put command.
        (input) data_dict -> Form-encoded data
        (input) **kwargs:
            None
        (output) Return status output of the command.

    """

    if data_dict:
        return requests.put("http://" + host + ":" + str(port) + cmd,
                            data=json.dumps(data_dict)).json()

    else:
        return requests.put("http://" + host + ":" + str(port) + cmd).json()
