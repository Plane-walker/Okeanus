from dock import Dock
import os
import requests
import json
from concurrent import futures
import grpc
import base64
import yaml
from interface.dci import dci_pb2_grpc
import unittest


class TestGraphData(unittest.TestCase):
    def test_graph_data(self):
        current_path = os.path.dirname(__file__)
        dock_config_path = os.path.join(current_path, 'config/dock.yaml')
        dock = Dock(dock_config_path)
        with open(dock.config_path) as file:
            config = yaml.load(file, Loader=yaml.Loader)
        for chain_name in config['chain_manager']['chain'].keys():
            dock.chain_manager.init_chain(chain_name)
            if not config['chain_manager']['chain'][chain_name]['join']:
                dock.chain_manager.add_chain(chain_name)
            else:
                dock.chain_manager.join_chain(chain_name)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        dci_pb2_grpc.add_DockServicer_to_server(dock.dock_server, server)
        host = config['dock']['address']['host']
        port = config['dock']['address']['port']
        server.add_insecure_port(f'{host}:{port}')
        server.start()
        message = {
            "header": {
                "type": "normal",
                "ttl": -1,
                "paths": [],
                "source_chain_id": "",
                "target_chain_id": "",
                "auth": {
                    "app_id": "1"
                }
            },
            "body": {
                "key": "test_key",
                "value": "test_value"
            }
        }
        params = (
            ('tx', '0x' + json.dumps(message).encode('utf-8').hex()),
        )
        requests.get(f"http://localhost:{config['chain_manager']['chain']['island_0']['rpc_port']}/broadcast_tx_commit", params=params)
        message = {
            "header": {
                "type": "normal",
                "ttl": -1,
                "paths": [],
                "source_chain_id": "",
                "target_chain_id": "",
                "auth": {
                    "app_id": "0"
                }
            },
            "body": {
                "query": "test_key",
            }
        }
        params = (
            ('data', '0x' + json.dumps(message).encode('utf-8').hex()),
        )
        requests.get(f"http://localhost:{config['chain_manager']['chain']['island_0']['rpc_port']}/abci_query", params=params)
        message = {
            "header": {
                "type": "graph",
                "ttl": -1,
                "paths": [],
                "source_chain_id": "",
                "target_chain_id": "",
                "auth": {
                    "app_id": "0"
                }
            },
            "body": {
                "query": "0",
            }
        }
        params = (
            ('data', '0x' + json.dumps(message).encode('utf-8').hex()),
        )
        response = requests.get(f"http://localhost:{config['chain_manager']['chain']['island_0']['rpc_port']}/abci_query", params=params)
        result = json.loads(base64.b64decode(json.loads(response.text)['result']['response']['value'].encode('utf-8')).decode('utf-8'))
        self.assertEqual(result[0]['source_app_id'], "0")
        self.assertEqual(result[0]['target_app_id'], "1")
        self.assertEqual(result[0]['weight'], 1)
        for chain in dock.chain_manager.select_chain(lambda single: True):
            dock.chain_manager.delete_chain(chain.chain_id)


if __name__ == '__main__':
    unittest.main()
