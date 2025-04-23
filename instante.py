import instaloader
import os
import shutil

print("[+] Bem-vindo ao Instant\n[+] Cole a URL do vídeo aqui")
url = input("[+]:")

L = instaloader.Instaloader()


shortcode = url.split('/')[-2]
print(f"[+] Shortcode extraído: {shortcode}")

try:
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, target=shortcode)
except Exception as e:
    print(f"[-] Erro ao acessar o post: {e}")
    exit(1)

video_dir = os.path.join(os.getcwd(), shortcode)

if os.path.exists(video_dir):
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]

    if video_files:
        video_path = os.path.join(video_dir, video_files[0])
        print(f"[+] Vídeo encontrado em: {video_path}")
        destino = os.path.expanduser('~/Downloads')
        caminho_destino = os.path.join(destino, video_files[0])

        try:
            shutil.move(video_path, caminho_destino)
            print(f"[+] Vídeo salvo em: {caminho_destino}")
        except Exception as e:
            print(f"[-] Erro ao mover o vídeo: {e}")

        try:
            shutil.rmtree(video_dir)
            print(f"[+] Pasta temporária '{shortcode}' removida.")
        except Exception as e:
            print(f"[-] Erro ao remover a pasta temporária: {e}")
    else:
        print("[-] Erro: Nenhum vídeo encontrado no diretório.")
else:
    print("[-] Erro: O diretório do vídeo não foi encontrado.")
