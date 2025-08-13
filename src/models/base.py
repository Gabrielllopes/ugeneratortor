from pydantic import BaseModel
from enum import StrEnum

class Language(StrEnum):
  ENGLISH = "English"
  SPANISH = "Spanish"
  PORTUGUESE = "Portuguese"
  FRENCH = "French"

class Carrossel(BaseModel):
  title: str
  slide: list[str]
  legend: str

ILUSTRATIONS_STYLE = {
  0 : "Handcrafted Knitted: Simulates textures of knitting, crochet, or handcrafted felt.",
  1 : "Fantasy Star: Epic aesthetic of classic RPGs and fantasy book covers.",
  2 : "LEGO: Colorful plastic blocks with a modular appearance.",
  3 : "Pixel Art: Visual style of 8-bit and 16-bit games, with retro charm.",
  4 : "DreamWorks: Caricatured 3D style typical of movies like Shrek and Kung Fu Panda.",
  5 : "Muppet: Puppet-like visuals, with textures resembling plush and fabric.",
  6 : "Attack on Titan: Inspired by the anime Shingeki no Kyojin, with bold and dark lines.",
  7 : "Fleischer Studios: 1930s style, like Betty Boop and Popeye.",
  8 : "Minecraft: Cubic block aesthetic typical of the Minecraft universe.",
  9 : "Simpsons: Visual style of the animated series, with yellow skin and exaggerated features.",
  10 : "Vintage Comic: Aesthetic of old comic books, like Marvel’s 1960s issues.",
  11 : "Cartoon Network: Visual style inspired by 2000s animations like Samurai Jack and others."
}