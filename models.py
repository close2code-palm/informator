from enum import IntEnum
from typing import Set

from sqlalchemy import Column, Integer, BigInteger, Text, \
    Boolean, SmallInteger, Enum, String, MetaData, Table, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

metadata = MetaData()


class Base(DeclarativeBase):
    metadata = metadata


user_specs = Table(
    'user_spec',
    Base.metadata,
    Column('user_id', ForeignKey('bot_users.uid'), primary_key=True),
    Column('spec_id', ForeignKey('spec.sid'), primary_key=True)
)


resource_specs = Table(
    'res_spec',
    Base.metadata,
    Column('res_id', ForeignKey('spec.sid'), primary_key=True),
    Column('spec_id', ForeignKey('info_source.r_id'), primary_key=True)
)


class Specialisation(Base):
    __tablename__ = 'spec'

    sid: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    naming: Mapped[str] = mapped_column(String(63))


class UserProfile(Base):
    __tablename__ = 'bot_users'

    uid = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    sex = Column(Boolean)
    age = Column(SmallInteger)
    full_name = Column(Text)
    address = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    social = Column(Text)
    specs: Mapped[Set['Specialisation']] = relationship(
        secondary=user_specs)


class ResourceType(IntEnum):
    SOCIAL_CHAT = 0
    CHANNEL = 1
    WEBSITE = 2
    LITERATURE = 3


class ResourceLevel(IntEnum):
    EASY = 0
    MEDIUM = 1
    HARD = 2


class Resource(Base):
    __tablename__ = 'info_source'

    r_id = Column(BigInteger, primary_key=True)
    r_type = Column(Enum(ResourceType))
    name = Column(String(63), nullable=False)
    link = Column(String(255))
    level = Column(Enum(ResourceLevel))
    priority = Column(SmallInteger)
    specs: Mapped[Set['Specialisation']] = relationship(
        secondary=resource_specs)
