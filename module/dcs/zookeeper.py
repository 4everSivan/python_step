import json

from kazoo.client import KazooClient


def test_kazoo(conn_lsn: dict) -> None:
    path_01 = '/service/test'
    path_02 = '/test/kazoo'
    client = KazooClient(conn_lsn['hosts'], conn_lsn['timeout'])
    client.start()

    try:
        # /
        root_children = client.get_children('/')

        # get children
        print("================ 1. get_children =================")
        path_01_children = client.get_children(path_01)
        print('type: {0} \n\npath_01_children: {1}\n'.format(type(path_01_children), path_01_children))

        # get
        print("================ 2. get =================")
        path_01_get = path_01 + '/' + path_01_children[0] + '/mmr_node'
        path_01_data = client.get(path_01_get)
        print('path: {0}\n'.format(path_01_get))
        print('type:{0} \n\npath_01_data: {1} \n\npath_01_znodestate: {2}\n'.format(
                type(path_01_data),
                path_01_data[0],
                path_01_data[1]
            )
        )

        # create
        print("================ 3. create =================")
        if 'test' not in root_children:
            data = 'i am path 02'
            encode_data = json.dumps(data).encode('utf-8')
            client.create(path_02, encode_data,  makepath=True)

            path_02_data = client.get(path_02)
            print('path_02_data: {0} \n\npath_02_znodestate: {1}\n'.format(path_02_data[0], path_02_data[1]))

        # set
        print("================ 4. update =================")
        root_children = client.get_children('/')
        if 'test' in root_children:
            before_update = client.get(path_02)
            data = 'i am path 02 update'
            encode_data = json.dumps(data).encode('utf-8')
            client.set(path_02, encode_data)
            after_update = client.get(path_02)
            print('before_update: {0} \n\nafter_update: {1}\n'.format(before_update[0], after_update[0]))

        # delete
        print("================ 5. delete =================")
        if 'test' in root_children:
            before_delete = client.get_children('/')
            client.delete('/test', recursive=True)
            after_delete = client.get_children('/')
            print('before_delete: {0} \n\nafter_delete: {1}'.format(before_delete, after_delete))

        # print node data
        print("================ 5. output patroni cluster data =================")
        output_znode_data(client, path_01)

        client.stop()
    except Exception as e:
        print(e)
        client.stop()


def output_znode_data(client: KazooClient, path: str) -> None:
    children = client.get_children(path)
    for child in children:
        child_path = path + '/' + child
        data, _ = client.get(child_path)
        print(f"Node: {child_path} " + '\n' + f"Data: {data.decode('utf-8')}")
        print(" ====================== " + '\n')
        output_znode_data(client, child_path)


if __name__ == '__main__':
    lsn = {
        "hosts": "172.16.245.4:2181,127.16.245.5:2181,172.16.245.6:2181",
        "timeout": 30
    }

    test_kazoo(lsn)



