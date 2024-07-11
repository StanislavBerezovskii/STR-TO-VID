import movis as mv
from os import path

from str_to_vid.settings import MEDIA_ROOT


def create_video_from_message(message: str):
    """
    This is the main project function creating a video from a message string
    :param message: str - message  to be converted into a video
    :return: mp4 video
    """
    if len(message) == 0:
        title = 'No message recieved'
    elif len(message) > 50:
        title = message[:50] + '...'
    else:
        title = message
    frame_size = (1920, 1080)
    text_layer = mv.layer.Text(message, font_size=256, font_family="Arial", color=(255, 255, 255))
    duration = (text_layer.get_size()[0] // frame_size[0] + 1) * 5

    scene = mv.layer.Composition(size=frame_size, duration=duration)
    scene.add_layer(mv.layer.Rectangle(scene.size, color=(0, 0, 0)))

    starting_position = scene.size[0] + text_layer.get_size()[0] // 2, scene.size[1] // 2

    scene.add_layer(
        text_layer,
        name="text",
        offset=0,
        position=starting_position,
        anchor_point=(0.0, 0.0),
        opacity=1.0,
        scale=1.0,
        rotation=0.0,
        blending_mode='normal',
    )
    ending_position = - text_layer.get_size()[0] // 2, scene.size[1] // 2
    scene['text'].position.enable_motion().extend(keyframes=[0.0, duration],
                                                  values=[starting_position, ending_position],
                                                  easings=['ease_in_out'])
    scene.write_video(dst_file=f'{MEDIA_ROOT}/{title}.mp4')
    return {'title': title, 'path': f'{MEDIA_ROOT}/{title}.mp4'}


def conversion_to_h264(video_file):
    """
    This function converts a video file to h264 format
    :param video_file: video file to be converted
    :return: h264 video
    """
    intro = mv.layer.Video(video_file)
    scene = mv.layer.Composition(size=(1920, 1080), duration=0.1)
    result = mv.concatenate([intro, scene])
    result.write_video(video_file)


def main():
    message = input('Введите текст бегущей строки: ')
    create_video_from_message(message)


if __name__ == '__main__':
    main()
