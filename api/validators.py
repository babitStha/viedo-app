from django.core.exceptions import ValidationError
from moviepy.editor import VideoFileClip
def validate_size(file):
    limit = 1 * 1024 * 1024 * 1024
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 GiB.')

def validate_file_type(value):
    if not (value.name.endswith('.mp4') or value.name.endswith('.mkv')):
        raise ValidationError('Only .mp4 or .mkv files are supported')

def validate_file_length(value):
    max_duration = 10 # in min
    clip = VideoFileClip(value.temporary_file_path())
    duration = clip.duration
    if duration >  max_duration * 60: #converting into seconds
        raise ValidationError("Video Length must be less than 10 min")
    