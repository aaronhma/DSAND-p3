class RouteTrieNode:
    def __init__(self):
        self.elements = dict()
        self.root_data = None

    def insert(self, data):
        if data not in self.elements:
            self.elements[data] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_data):
        self.root = RouteTrieNode()
        self.root_data = root_data

    def insert(self, path, about):
        root = self.root

        for i in path:
            root.insert(i)
            root = root.elements[i]

        root.root_data = about

    def find(self, path):
        root = self.root

        for i in path:
            if i not in root.elements:
                return -1

            root = root.elements[i]

        return root.root_data


class Router:
    def __init__(self, root_data, not_found):
        self.router = RouteTrie(root_data)
        self.not_found = not_found
        self.root_data = root_data

    def add_handler(self, path, about):
        self.router.insert(self.split_path(path), about)

    def lookup(self, path):
        if path == "/":
            return self.root_data

        if len(self.split_path(path)) == 0:
            return self.router.handler

        web_page = self.router.find(self.split_path(path))

        if web_page == -1:
            return self.not_found

        else:
            return web_page

    def split_path(self, path):
        split = list()

        for i in path.split(sep='/'):
            if i != ' ':
                split.append(i)

        return split


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
