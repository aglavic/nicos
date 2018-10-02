# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers


class EventHistogram(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEventHistogram(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventHistogram()
        x.Init(buf, n + offset)
        return x

    # EventHistogram
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventHistogram
    def Source(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # EventHistogram
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # EventHistogram
    def DimMetadata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .DimensionMetaData import DimensionMetaData
            obj = DimensionMetaData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # EventHistogram
    def DimMetadataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventHistogram
    def LastMetadataTimestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # EventHistogram
    def CurrentShape(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventHistogram
    def CurrentShapeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # EventHistogram
    def CurrentShapeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventHistogram
    def Offset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventHistogram
    def OffsetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # EventHistogram
    def OffsetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventHistogram
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # EventHistogram
    def Data(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # EventHistogram
    def ErrorsType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # EventHistogram
    def Errors(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # EventHistogram
    def Info(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def EventHistogramStart(builder): builder.StartObject(11)
def EventHistogramAddSource(builder, source): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(source), 0)
def EventHistogramAddTimestamp(builder, timestamp): builder.PrependUint64Slot(1, timestamp, 0)
def EventHistogramAddDimMetadata(builder, dimMetadata): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(dimMetadata), 0)
def EventHistogramStartDimMetadataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventHistogramAddLastMetadataTimestamp(builder, lastMetadataTimestamp): builder.PrependUint64Slot(3, lastMetadataTimestamp, 0)
def EventHistogramAddCurrentShape(builder, currentShape): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(currentShape), 0)
def EventHistogramStartCurrentShapeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventHistogramAddOffset(builder, offset): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(offset), 0)
def EventHistogramStartOffsetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventHistogramAddDataType(builder, dataType): builder.PrependUint8Slot(6, dataType, 0)
def EventHistogramAddData(builder, data): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def EventHistogramAddErrorsType(builder, errorsType): builder.PrependUint8Slot(8, errorsType, 0)
def EventHistogramAddErrors(builder, errors): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(errors), 0)
def EventHistogramAddInfo(builder, info): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(info), 0)
def EventHistogramEnd(builder): return builder.EndObject()
