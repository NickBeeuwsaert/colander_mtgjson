
def _get_key(node):
    try:
        rename = node.rename
    except:
        rename = node.name
    return rename

class RenameMixin:
    """Renames a Mapping schemas nodes based on their rename property"""
    def serialize(self, appstruct):
        translation = {
            node.name: _get_key(node)
            for node in self.children
            if hasattr(node, 'rename')
        }
        cstruct = super().serialize(appstruct)

        return {
            translation.get(key, key): value
            for key, value in cstruct.items()
        }

    def deserialize(self, cstruct):
        translation = {
            _get_key(node): node.name
            for node in self.children
            if hasattr(node, 'rename')
        }
        
        return super().deserialize({
            translation.get(key, key): value
            for key, value in cstruct.items()
        })
