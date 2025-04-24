from fastapi import Depends, FastAPI
from fastapi.responses import StreamingResponse
from typing import cast, IO

from micro_llm.domain.domain import Domain
from micro_llm.domain.entities.chat_message import ChatMessage


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/query")
    async def query_llm(  # pyright: ignore[reportUnusedFunction]
        chat_messages: list[ChatMessage],
        _: User = Depends(validate_user_wrapper(domain))
    ) -> VideoDto:
        video = domain.get_video_with_formats(video_id)

        audio_format_dtos = [
            AudioFormatDto(
                id=audio_format.id,
                url=audio_format.url,
                codec=audio_format.codec,
                abr=audio_format.abr,
            )
            for audio_format in video.audio_formats
        ]
        video_format_dtos = [
            VideoFormatDto(
                id=video_format.id,
                url=video_format.url,
                codec=video_format.codec,
                height=video_format.height,
                width=video_format.width,
                fps=video_format.fps,
            )
            for video_format in video.video_formats
        ]
        return VideoDto(
            id=video.id,
            title=video.title,
            channel_id=video.channel_id,
            channel_title=video.channel_title,
            thumbnail_url=video.thumbnail_url,
            duration=video.duration,
            view_count=video.view_count,
            upload_date=video.upload_date,
            audio_formats=audio_format_dtos,
            video_formats=video_format_dtos,
        )
