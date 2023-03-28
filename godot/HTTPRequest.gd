extends HTTPRequest


# Called when the node enters the scene tree for the first time.
func _ready():
	print(" Helloo")
	self.use_threads = true
	self.connect("request_completed", response
	var data = self.request("http://www.mocky.io/v2/5185415ba171ea3a00704eed")
	pass


func response(result, response_code, headers, body):
	print(body.get_string_from_utf8())

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
