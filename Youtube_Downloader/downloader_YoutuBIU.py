# %% [markdown]
# # <font color='#7ED957'>**Baixar vídeos do Youtube**</font>

# %%
from pytube import YouTube

youtube = YouTube('https://youtu.be/e-fNXcdDKNg')

youtube.streams.get_highest_resolution().download()

# %% [markdown]
# ### <font color='##C9E265'>**Baixar áudio e converter para .MP3**</font>
# 
# ATENÇÃO: necessário passar o caminho da pasta, onde deseja salvar o arquivo.
# 
# * **Exemplo: D:\Users\Micro3\Downloads**

# %%
from pytube import YouTube
import os
yt = YouTube(str(input("Digite o URL do vídeo do youtube: \n ")))
video = yt.streams.filter(only_audio=True).first()
print("Digite o endereço de destino (deixe em branco para salvar no diretório atual)")
destination = str(input(" ")) or '.'
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title + " Áudio baixado com sucesso!")


