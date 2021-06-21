from dp_python_helper.config_module import Configuration

c = Configuration()
c.read_yaml("cfg")
c.read_json("cfg")
print(c.env1)
print(c["env1"])
print(c.env2["test3"].test4)

# Output:
# Configuration{
#   "foo": [
#     "bar"
#   ],
#   "spam": {
#     "eggs": "Hello json"
#   }
# }
#
# Configuration{
#   "foo": [
#     "bar"
#   ],
#   "spam": {
#     "eggs": "Hello json"
#   }
# }
#
# this is
