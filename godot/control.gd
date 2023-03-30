extends Control

var ultimoID = 0
var loading_screen = preload("res://loading.tscn")
var instance = loading_screen.instantiate()
var redDotLastX = 0
var redDotLastY = 0
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
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	placeRedDot(response["coordinates"])
	print(response)

		#ultimo ID
	ultimoID = response["joints"][0]["id"]
		#junta1
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta1container/ProgressBar.value=response["joints"][0]["j1"]
		#junta2
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta2container/ProgressBar.value=response["joints"][0]["j2"]
		#junta3
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/junta3container/ProgressBar.value=response["joints"][0]["j3"]

		#ultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar7.value=response["joints"][0]["j1"]
		#ultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar8.value=response["joints"][0]["j2"]
		#ultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar9.value=response["joints"][0]["j3"]
	
		#penultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar1.value=response["joints"][1]["j1"]
		#penultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar2.value=response["joints"][1]["j2"]
		#penultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar3.value=response["joints"][1]["j3"]
	
		#antepenultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar4.value=response["joints"][2]["j1"]
		#antepenultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar5.value=response["joints"][2]["j2"]
		#antepenultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar6.value=response["joints"][2]["j3"]

	instance.queue_free()
	instance = loading_screen.instantiate()

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
	print(ultimoID -1)
	makePost(ultimoID -1)


func _on_voltar_antepenultima_pressed():
	makePost(ultimoID - 2)


func _on_repetir_pressed():
	add_child(instance)
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	var error = http_request.request("http://127.0.0.1:3000/repeatLastPositions")
	if error != OK:
		push_error("An error occurred in the HTTP request.")

# função para o visualizador de posição da garra
func placeRedDot(data):
	$Container/Ellipse2.move_local_y(-redDotLastY)
	$Container/Ellipse2.move_local_x(-redDotLastX)
	
	$Container/Ellipse2.move_local_y(-data[0] / 1.7)
	$Container/Ellipse2.move_local_x(-data[1]  /2)
	redDotLastY = -data[0] / 1.7
	redDotLastX = -data[1] / 2
