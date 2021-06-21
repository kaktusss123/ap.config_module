from dp_python_helper.config_module import Configuration

c = Configuration()
c.read_yaml()
print(c)

# Output:
# WARNING:root:Config 'example.broken.yml' doesn't match the environment
# Configuration{
#   "example": {
#     "field1": {
#       "nested_filed1": "hello world",
#       "nested_field2": {
#         "nested_filed3": "foo",
#         "nested_field4": "bar"
#       }
#     }
#   }
# }
