import movis as mv
from os import path

from str_to_vid.settings import MEDIA_ROOT


def create_video_from_message(message: str):
    """
    This is the main project function creating a video from a message string
    :param message: str - message  to be converted into a video
    :return: mp4 video
    """
    # checks if message parameter is empty
    if len(message) == 0:
        title = 'No message recieved'
    elif len(message) > 50:
        title = message[:50] + '...'
    else:
        # sets the name for the video
        title = message
    # sets video frame size
    frame_size = (1920, 1080)
    # creates the text layer with the message text, in specific font and color white
    text_layer = mv.layer.Text(message, font_size=256, font_family="Arial", color=(255, 255, 255))

    # sets the duration of the video based on the width of the text layer and the frame size
    duration = (text_layer.get_size()[0] // frame_size[0] + 1) * 5

    # creates the video scene - a Composition object with our frame size and duration
    scene = mv.layer.Composition(size=frame_size, duration=duration)
    # creates a black background for the scene
    scene.add_layer(mv.layer.Rectangle(scene.size, color=(0, 0, 0)))

    # sets the starting position of the text layer
    starting_position = scene.size[0] + text_layer.get_size()[0] // 2, scene.size[1] // 2

    # adds the text layer to the scene with parameters
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
    # calculates the ending position of a text layer in a video scene
    ending_position = - text_layer.get_size()[0] // 2, scene.size[1] // 2
    # enables motion on of the text layer from the starting position to the ending position
    scene['text'].position.enable_motion().extend(keyframes=[0.0, duration],
                                                  values=[starting_position, ending_position],
                                                  easings=['ease_in_out'])
    # writes the video scene to a file located at the path specified by MEDIA_ROOT
    scene.write_video(dst_file=f'{MEDIA_ROOT}/{title}.mp4')
    # returns the video title and the path to the video file
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
