import subprocess

def obtener_info_hdmi():
    resultado = subprocess.check_output(["xrandr"])
    separacion = resultado.decode("utf-8").split("\n")
    print(separacion)
    return resultado.decode("utf-8")

obtener_info_hdmi()