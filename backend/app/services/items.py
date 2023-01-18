from os import getenv 

from slugify import slugify
from dotenv import load_dotenv
import openai

from app.db.errors import EntityDoesNotExist
from app.db.repositories.items import ItemsRepository
from app.models.domain.items import Item
from app.models.domain.users import User

load_dotenv()
openai.api_key = getenv("OPENAI_API_KEY")

async def check_item_exists(items_repo: ItemsRepository, slug: str) -> bool:
    try:
        await items_repo.get_item_by_slug(slug=slug)
    except EntityDoesNotExist:
        return False

    return True


def get_slug_for_item(title: str) -> str:
    return slugify(title)


def check_user_can_modify_item(item: Item, user: User) -> bool:
    return item.seller.username == user.username

def generate_image(prompt: str) -> str:
    return openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )['data'][0]['url']