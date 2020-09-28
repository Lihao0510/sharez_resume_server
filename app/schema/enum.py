from enum import Enum


# { code: 1, name: '模块与列表关联' },
# { code: 2, name: '模块与详情关联' },
# { code: 3, name: '列表与表单关联' },
# { code: 4, name: '详情与表单关联' }
class RelationType(Enum):
    MODULE_LIST_RELATION = 1
    MODULE_DETAIL_RELATION = 2
    LIST_FORM_RELATION = 3
    DETAIL_FORM_RELATION = 4
