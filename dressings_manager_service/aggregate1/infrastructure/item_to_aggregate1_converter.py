from dressings_manager_service.aggregate1.domain.aggregate1 import Aggregate1
from dressings_manager_service.entrypoint.items.aggregate1_item import Aggregate1Item


def invoke(aggregate1_item: Aggregate1Item) -> Aggregate1:
    return Aggregate1(
        aggregate1_item.id_,
        aggregate1_item.param1,
    )