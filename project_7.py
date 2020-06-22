class Router:
    def __init__(self, root, not_found):
        self.root = root
        self.not_found = not_found
        self.routes = [["/", root]]

    def add_handler(self, route, content):
        if "/" != route[-1]:
            router = route + "/"
            self.routes.append([router, content])

        self.routes.append([route, content])

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        for i in self.routes:
            # for j in i:
            if i[0] == route:
                return i[1]
            # print(j[0])
            # print(j[1])
            # if j[0] == route:
            # return j[1]

        return self.not_found

    # def split_path(self):
    #     # you need to split the path into parts for
    #     # both the add_handler and loopup functions,
    #     # so it should be placed in a function here

    #     # Here are some test cases and expected outputs you can use to test your implementation

    #     # create the router and add a route
    #     # remove the 'not found handler' if you did not implement this
    #     pass


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
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
