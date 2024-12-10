from moviepy.video.io.VideoFileClip import VideoFileClip

def cut_video(input_video_path, output_video_path, start_time, end_time, frame_width, frame_height, bitrate, fps):
    with VideoFileClip(input_video_path) as video:
        
        new_video = video.subclipped(start_time, end_time)

        new_video.write_videofile(output_video_path, codec='libx264', bitrate=bitrate, fps=fps)

input_path = './dragon.mp4'    # Đường dẫn đến video gốc
output_path = './dragon_cut.mp4' # Đường dẫn để lưu video đã cắt
start = 0                       # Thời gian bắt đầu (giây)
end = 19                         # Thời gian kết thúc (giây)
frame_width = 1920               # Chiều rộng khung hình
frame_height = 1080               # Chiều cao khung hình
bitrate = '5006k'                # Tốc độ dữ liệu
fps = 30                         # Tốc độ khung hình

cut_video(input_path, output_path, start, end, frame_width, frame_height, bitrate, fps)