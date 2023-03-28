extends Control

var ultimoID = 0
var penultimoID = 0
var loading_screen = preload("res://loading.tscn")
var instance = loading_screen.instantiate()
# Called when the node enters the scene tree for the first time.
func _ready():
	pass

func _on_atualizar_pressed():
	add_child(instance)
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._get_request_completed)
	var error = http_request.request("http://127.0.0.1:3000/getLastPositions")
	if error != OK:
		push_error("An error occurred in the HTTP request.")

func _get_request_completed(result, response_code, headers, body):
	instance.queue_free()
	instance = loading_screen.instantiate()
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	print(response)


		#junta1
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta1container/ProgressBar.value=response[0]["j1"]
		#junta2
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta2container/ProgressBar.value=response[0]["j2"]
		#junta3
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/junta3container/ProgressBar.value=response[0]["j3"]

		#ultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar1.value=response[1]["j1"]
		#ultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar2.value=response[1]["j2"]
		#ultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar3.value=response[1]["j3"]
	ultimoID = response[1]["id"]
	
		#penultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar4.value=response[2]["j1"]
		#penultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar5.value=response[2]["j2"]
		#penultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar6.value=response[2]["j3"]
	penultimoID = response[2]["id"]


func makePost(id: int):
	add_child(instance)
	var link = "http://127.0.0.1:3000/move"
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	var body = JSON.new().stringify({"id": id})
	var error = http_request.request(link, [], HTTPClient.METHOD_POST, body)
	if error != OK:
		push_error("An error occurred in the HTTP request.")

func _http_request_completed(result, response_code, headers, body):
	instance.queue_free()
	instance = loading_screen.instantiate()
	
	
func _on_voltar_ultima_pressed():
	print(ultimoID)
	makePost(ultimoID)


func _on_voltar_penultima_pressed():
	print(penultimoID)
	makePost(penultimoID)
