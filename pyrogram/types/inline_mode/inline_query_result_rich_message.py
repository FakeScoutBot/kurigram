#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Optional

import pyrogram
from pyrogram import raw, types

from .inline_query_result import InlineQueryResult


class InlineQueryResultRichMessage(InlineQueryResult):
    """Represents an inline query result that sends a rich-formatted message.

    When a user selects this result, a rich message is sent using
    :tl:`InputBotInlineMessageRichMessage`.

    Parameters:
        title (``str``):
            Title of the result shown in the inline list.

        html (``str``, *optional*):
            Rich HTML content for the sent message.
            Exactly one of ``html`` or ``markdown`` must be provided.

        markdown (``str``, *optional*):
            Rich Markdown (GFM-style) content for the sent message.
            Exactly one of ``html`` or ``markdown`` must be provided.

        id (``str``, *optional*):
            Unique identifier for this result, 1-64 bytes.
            Defaults to a random UUID.

        description (``str``, *optional*):
            Short description of the result shown in the inline list.

        is_rtl (``bool``, *optional*):
            Pass True if the rich message should be rendered right-to-left.

        skip_entity_detection (``bool``, *optional*):
            Pass True to disable automatic entity detection (URLs, mentions, etc.)
            in the rich message text.

        reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the sent message.

    Example:
        .. code-block:: python

            from pyrogram.types import InlineQueryResultRichMessage

            @app.on_inline_query()
            async def handler(client, query):
                results = [
                    InlineQueryResultRichMessage(
                        title="Rich Article",
                        description="Tap to send rich content",
                        html="<h1>Hello</h1><p>This is a <b>rich</b> message.</p>",
                    )
                ]
                await query.answer(results)
    """

    def __init__(
        self,
        title: str,
        html: Optional[str] = None,
        markdown: Optional[str] = None,
        id: Optional[str] = None,
        description: Optional[str] = None,
        is_rtl: Optional[bool] = None,
        skip_entity_detection: Optional[bool] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
    ):
        if not html and not markdown:
            raise ValueError("Either `html` or `markdown` must be provided")
        if html and markdown:
            raise ValueError("Only one of `html` or `markdown` can be provided, not both")

        super().__init__(
            "article",
            id,
            types.InputRichMessageContent(
                rich_message=types.InputRichMessage(
                    html=html,
                    markdown=markdown,
                    is_rtl=is_rtl,
                    skip_entity_detection=skip_entity_detection,
                )
            ),
            reply_markup,
        )

        self.title = title
        self.description = description

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputBotInlineResult(
            id=self.id,
            type=self.type,
            send_message=await self.input_message_content.write(client, self.reply_markup),
            title=self.title,
            description=self.description,
        )