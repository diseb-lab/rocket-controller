# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ripple.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protos/ripple.proto\x12\x08protocol\"\x1e\n\nTMManifest\x12\x10\n\x08stobject\x18\x01 \x02(\x0c\"F\n\x0bTMManifests\x12\"\n\x04list\x18\x01 \x03(\x0b\x32\x14.protocol.TMManifest\x12\x13\n\x07history\x18\x02 \x01(\x08\x42\x02\x18\x01\"k\n\rTMClusterNode\x12\x11\n\tpublicKey\x18\x01 \x02(\t\x12\x12\n\nreportTime\x18\x02 \x02(\r\x12\x10\n\x08nodeLoad\x18\x03 \x02(\r\x12\x10\n\x08nodeName\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\"9\n\x0cTMLoadSource\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x63ost\x18\x02 \x02(\r\x12\r\n\x05\x63ount\x18\x03 \x01(\r\"g\n\tTMCluster\x12-\n\x0c\x63lusterNodes\x18\x01 \x03(\x0b\x32\x17.protocol.TMClusterNode\x12+\n\x0bloadSources\x18\x02 \x03(\x0b\x32\x16.protocol.TMLoadSource\"O\n\x0eTMGetShardInfo\x12\x10\n\x04hops\x18\x01 \x02(\rB\x02\x18\x01\x12\x14\n\x08lastLink\x18\x02 \x01(\x08\x42\x02\x18\x01\x12\x15\n\tpeerchain\x18\x03 \x03(\rB\x02\x18\x01\"\x82\x01\n\x0bTMShardInfo\x12\x18\n\x0cshardIndexes\x18\x01 \x02(\tB\x02\x18\x01\x12\x16\n\nnodePubKey\x18\x02 \x01(\x0c\x42\x02\x18\x01\x12\x14\n\x08\x65ndpoint\x18\x03 \x01(\tB\x02\x18\x01\x12\x14\n\x08lastLink\x18\x04 \x01(\x08\x42\x02\x18\x01\x12\x15\n\tpeerchain\x18\x05 \x03(\rB\x02\x18\x01\"\x1c\n\x06TMLink\x12\x12\n\nnodePubKey\x18\x01 \x02(\x0c\"Y\n\x12TMGetPeerShardInfo\x12\x0c\n\x04hops\x18\x01 \x02(\r\x12\x10\n\x08lastLink\x18\x02 \x01(\x08\x12#\n\tpeerChain\x18\x03 \x03(\x0b\x32\x10.protocol.TMLink\"\x84\x01\n\x0fTMPeerShardInfo\x12\x14\n\x0cshardIndexes\x18\x01 \x02(\t\x12\x12\n\nnodePubKey\x18\x02 \x01(\x0c\x12\x10\n\x08\x65ndpoint\x18\x03 \x01(\t\x12\x10\n\x08lastLink\x18\x04 \x01(\x08\x12#\n\tpeerChain\x18\x05 \x03(\x0b\x32\x10.protocol.TMLink\"\x80\x01\n\rTMTransaction\x12\x16\n\x0erawTransaction\x18\x01 \x02(\x0c\x12+\n\x06status\x18\x02 \x02(\x0e\x32\x1b.protocol.TransactionStatus\x12\x18\n\x10receiveTimestamp\x18\x03 \x01(\x04\x12\x10\n\x08\x64\x65\x66\x65rred\x18\x04 \x01(\x08\"\xdb\x01\n\x0eTMStatusChange\x12\'\n\tnewStatus\x18\x01 \x01(\x0e\x32\x14.protocol.NodeStatus\x12%\n\x08newEvent\x18\x02 \x01(\x0e\x32\x13.protocol.NodeEvent\x12\x11\n\tledgerSeq\x18\x03 \x01(\r\x12\x12\n\nledgerHash\x18\x04 \x01(\x0c\x12\x1a\n\x12ledgerHashPrevious\x18\x05 \x01(\x0c\x12\x13\n\x0bnetworkTime\x18\x06 \x01(\x04\x12\x10\n\x08\x66irstSeq\x18\x07 \x01(\r\x12\x0f\n\x07lastSeq\x18\x08 \x01(\r\"\xf3\x01\n\x0cTMProposeSet\x12\x12\n\nproposeSeq\x18\x01 \x02(\r\x12\x15\n\rcurrentTxHash\x18\x02 \x02(\x0c\x12\x12\n\nnodePubKey\x18\x03 \x02(\x0c\x12\x11\n\tcloseTime\x18\x04 \x02(\r\x12\x11\n\tsignature\x18\x05 \x02(\x0c\x12\x16\n\x0epreviousledger\x18\x06 \x02(\x0c\x12\x19\n\x11\x61\x64\x64\x65\x64Transactions\x18\n \x03(\x0c\x12\x1b\n\x13removedTransactions\x18\x0b \x03(\x0c\x12\x1c\n\x10\x63heckedSignature\x18\x07 \x01(\x08\x42\x02\x18\x01\x12\x10\n\x04hops\x18\x0c \x01(\rB\x02\x18\x01\"K\n\x14TMHaveTransactionSet\x12%\n\x06status\x18\x01 \x02(\x0e\x32\x15.protocol.TxSetStatus\x12\x0c\n\x04hash\x18\x02 \x02(\x0c\"U\n\x0fTMValidatorList\x12\x10\n\x08manifest\x18\x01 \x02(\x0c\x12\x0c\n\x04\x62lob\x18\x02 \x02(\x0c\x12\x11\n\tsignature\x18\x03 \x02(\x0c\x12\x0f\n\x07version\x18\x04 \x02(\r\"F\n\x11ValidatorBlobInfo\x12\x10\n\x08manifest\x18\x01 \x01(\x0c\x12\x0c\n\x04\x62lob\x18\x02 \x02(\x0c\x12\x11\n\tsignature\x18\x03 \x02(\x0c\"j\n\x19TMValidatorListCollection\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\x10\n\x08manifest\x18\x02 \x02(\x0c\x12*\n\x05\x62lobs\x18\x03 \x03(\x0b\x32\x1b.protocol.ValidatorBlobInfo\"R\n\x0cTMValidation\x12\x12\n\nvalidation\x18\x01 \x02(\x0c\x12\x1c\n\x10\x63heckedSignature\x18\x02 \x01(\x08\x42\x02\x18\x01\x12\x10\n\x04hops\x18\x03 \x01(\rB\x02\x18\x01\"\x8e\x01\n\x0bTMEndpoints\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\x38\n\x0c\x65ndpoints_v2\x18\x03 \x03(\x0b\x32\".protocol.TMEndpoints.TMEndpointv2\x1a.\n\x0cTMEndpointv2\x12\x10\n\x08\x65ndpoint\x18\x01 \x02(\t\x12\x0c\n\x04hops\x18\x02 \x02(\rJ\x04\x08\x02\x10\x03\"_\n\x0fTMIndexedObject\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x0e\n\x06nodeID\x18\x02 \x01(\x0c\x12\r\n\x05index\x18\x03 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x11\n\tledgerSeq\x18\x05 \x01(\r\"\xbf\x02\n\x11TMGetObjectByHash\x12\x34\n\x04type\x18\x01 \x02(\x0e\x32&.protocol.TMGetObjectByHash.ObjectType\x12\r\n\x05query\x18\x02 \x02(\x08\x12\x0b\n\x03seq\x18\x03 \x01(\r\x12\x12\n\nledgerHash\x18\x04 \x01(\x0c\x12\x0b\n\x03\x66\x61t\x18\x05 \x01(\x08\x12*\n\x07objects\x18\x06 \x03(\x0b\x32\x19.protocol.TMIndexedObject\"\x8a\x01\n\nObjectType\x12\r\n\totUNKNOWN\x10\x00\x12\x0c\n\x08otLEDGER\x10\x01\x12\x11\n\rotTRANSACTION\x10\x02\x12\x16\n\x12otTRANSACTION_NODE\x10\x03\x12\x10\n\x0cotSTATE_NODE\x10\x04\x12\x10\n\x0cotCAS_OBJECT\x10\x05\x12\x10\n\x0cotFETCH_PACK\x10\x06\"0\n\x0cTMLedgerNode\x12\x10\n\x08nodedata\x18\x01 \x02(\x0c\x12\x0e\n\x06nodeid\x18\x02 \x01(\x0c\"\xec\x01\n\x0bTMGetLedger\x12)\n\x05itype\x18\x01 \x02(\x0e\x32\x1a.protocol.TMLedgerInfoType\x12%\n\x05ltype\x18\x02 \x01(\x0e\x32\x16.protocol.TMLedgerType\x12\x12\n\nledgerHash\x18\x03 \x01(\x0c\x12\x11\n\tledgerSeq\x18\x04 \x01(\r\x12\x0f\n\x07nodeIDs\x18\x05 \x03(\x0c\x12\x15\n\rrequestCookie\x18\x06 \x01(\x04\x12(\n\tqueryType\x18\x07 \x01(\x0e\x32\x15.protocol.TMQueryType\x12\x12\n\nqueryDepth\x18\x08 \x01(\r\"\xc4\x01\n\x0cTMLedgerData\x12\x12\n\nledgerHash\x18\x01 \x02(\x0c\x12\x11\n\tledgerSeq\x18\x02 \x02(\r\x12(\n\x04type\x18\x03 \x02(\x0e\x32\x1a.protocol.TMLedgerInfoType\x12%\n\x05nodes\x18\x04 \x03(\x0b\x32\x16.protocol.TMLedgerNode\x12\x15\n\rrequestCookie\x18\x05 \x01(\r\x12%\n\x05\x65rror\x18\x06 \x01(\x0e\x32\x16.protocol.TMReplyError\"\x85\x01\n\x06TMPing\x12\'\n\x04type\x18\x01 \x02(\x0e\x32\x19.protocol.TMPing.pingType\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x10\n\x08pingTime\x18\x03 \x01(\x04\x12\x0f\n\x07netTime\x18\x04 \x01(\x04\"\"\n\x08pingType\x12\n\n\x06ptPING\x10\x00\x12\n\n\x06ptPONG\x10\x01\"N\n\tTMSquelch\x12\x0f\n\x07squelch\x18\x01 \x02(\x08\x12\x17\n\x0fvalidatorPubKey\x18\x02 \x02(\x0c\x12\x17\n\x0fsquelchDuration\x18\x03 \x01(\r\"^\n\x12TMProofPathRequest\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\x12\n\nledgerHash\x18\x02 \x02(\x0c\x12\'\n\x04type\x18\x03 \x02(\x0e\x32\x19.protocol.TMLedgerMapType\"\xaa\x01\n\x13TMProofPathResponse\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\x12\n\nledgerHash\x18\x02 \x02(\x0c\x12\'\n\x04type\x18\x03 \x02(\x0e\x32\x19.protocol.TMLedgerMapType\x12\x14\n\x0cledgerHeader\x18\x04 \x01(\x0c\x12\x0c\n\x04path\x18\x05 \x03(\x0c\x12%\n\x05\x65rror\x18\x06 \x01(\x0e\x32\x16.protocol.TMReplyError\"*\n\x14TMReplayDeltaRequest\x12\x12\n\nledgerHash\x18\x01 \x02(\x0c\"}\n\x15TMReplayDeltaResponse\x12\x12\n\nledgerHash\x18\x01 \x02(\x0c\x12\x14\n\x0cledgerHeader\x18\x02 \x01(\x0c\x12\x13\n\x0btransaction\x18\x03 \x03(\x0c\x12%\n\x05\x65rror\x18\x04 \x01(\x0e\x32\x16.protocol.TMReplyError*\xe5\x03\n\x0bMessageType\x12\x0f\n\x0bmtMANIFESTS\x10\x02\x12\n\n\x06mtPING\x10\x03\x12\r\n\tmtCLUSTER\x10\x05\x12\x0f\n\x0bmtENDPOINTS\x10\x0f\x12\x11\n\rmtTRANSACTION\x10\x1e\x12\x10\n\x0cmtGET_LEDGER\x10\x1f\x12\x11\n\rmtLEDGER_DATA\x10 \x12\x14\n\x10mtPROPOSE_LEDGER\x10!\x12\x13\n\x0fmtSTATUS_CHANGE\x10\"\x12\x0e\n\nmtHAVE_SET\x10#\x12\x10\n\x0cmtVALIDATION\x10)\x12\x11\n\rmtGET_OBJECTS\x10*\x12\x14\n\x10mtGET_SHARD_INFO\x10\x32\x12\x10\n\x0cmtSHARD_INFO\x10\x33\x12\x19\n\x15mtGET_PEER_SHARD_INFO\x10\x34\x12\x15\n\x11mtPEER_SHARD_INFO\x10\x35\x12\x13\n\x0fmtVALIDATORLIST\x10\x36\x12\r\n\tmtSQUELCH\x10\x37\x12\x1d\n\x19mtVALIDATORLISTCOLLECTION\x10\x38\x12\x14\n\x10mtPROOF_PATH_REQ\x10\x39\x12\x19\n\x15mtPROOF_PATH_RESPONSE\x10:\x12\x16\n\x12mtREPLAY_DELTA_REQ\x10;\x12\x1b\n\x17mtREPLAY_DELTA_RESPONSE\x10<*\xa1\x01\n\x11TransactionStatus\x12\t\n\x05tsNEW\x10\x01\x12\r\n\ttsCURRENT\x10\x02\x12\x0e\n\ntsCOMMITED\x10\x03\x12\x15\n\x11tsREJECT_CONFLICT\x10\x04\x12\x14\n\x10tsREJECT_INVALID\x10\x05\x12\x12\n\x0etsREJECT_FUNDS\x10\x06\x12\x0e\n\ntsHELD_SEQ\x10\x07\x12\x11\n\rtsHELD_LEDGER\x10\x08*c\n\nNodeStatus\x12\x10\n\x0cnsCONNECTING\x10\x01\x12\x0f\n\x0bnsCONNECTED\x10\x02\x12\x10\n\x0cnsMONITORING\x10\x03\x12\x10\n\x0cnsVALIDATING\x10\x04\x12\x0e\n\nnsSHUTTING\x10\x05*`\n\tNodeEvent\x12\x14\n\x10neCLOSING_LEDGER\x10\x01\x12\x15\n\x11neACCEPTED_LEDGER\x10\x02\x12\x15\n\x11neSWITCHED_LEDGER\x10\x03\x12\x0f\n\x0bneLOST_SYNC\x10\x04*4\n\x0bTxSetStatus\x12\n\n\x06tsHAVE\x10\x01\x12\r\n\ttsCAN_GET\x10\x02\x12\n\n\x06tsNEED\x10\x03*P\n\x10TMLedgerInfoType\x12\n\n\x06liBASE\x10\x00\x12\r\n\tliTX_NODE\x10\x01\x12\r\n\tliAS_NODE\x10\x02\x12\x12\n\x0eliTS_CANDIDATE\x10\x03*;\n\x0cTMLedgerType\x12\x0e\n\nltACCEPTED\x10\x00\x12\r\n\tltCURRENT\x10\x01\x12\x0c\n\x08ltCLOSED\x10\x02*\x1d\n\x0bTMQueryType\x12\x0e\n\nqtINDIRECT\x10\x00*A\n\x0cTMReplyError\x12\x0f\n\x0breNO_LEDGER\x10\x01\x12\r\n\treNO_NODE\x10\x02\x12\x11\n\rreBAD_REQUEST\x10\x03*9\n\x0fTMLedgerMapType\x12\x11\n\rlmTRANASCTION\x10\x01\x12\x13\n\x0flmACCOUNT_STATE\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.ripple_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_TMMANIFESTS'].fields_by_name['history']._loaded_options = None
    _globals['_TMMANIFESTS'].fields_by_name['history']._serialized_options = b'\030\001'
    _globals['_TMGETSHARDINFO'].fields_by_name['hops']._loaded_options = None
    _globals['_TMGETSHARDINFO'].fields_by_name['hops']._serialized_options = b'\030\001'
    _globals['_TMGETSHARDINFO'].fields_by_name['lastLink']._loaded_options = None
    _globals['_TMGETSHARDINFO'].fields_by_name['lastLink']._serialized_options = b'\030\001'
    _globals['_TMGETSHARDINFO'].fields_by_name['peerchain']._loaded_options = None
    _globals['_TMGETSHARDINFO'].fields_by_name['peerchain']._serialized_options = b'\030\001'
    _globals['_TMSHARDINFO'].fields_by_name['shardIndexes']._loaded_options = None
    _globals['_TMSHARDINFO'].fields_by_name['shardIndexes']._serialized_options = b'\030\001'
    _globals['_TMSHARDINFO'].fields_by_name['nodePubKey']._loaded_options = None
    _globals['_TMSHARDINFO'].fields_by_name['nodePubKey']._serialized_options = b'\030\001'
    _globals['_TMSHARDINFO'].fields_by_name['endpoint']._loaded_options = None
    _globals['_TMSHARDINFO'].fields_by_name['endpoint']._serialized_options = b'\030\001'
    _globals['_TMSHARDINFO'].fields_by_name['lastLink']._loaded_options = None
    _globals['_TMSHARDINFO'].fields_by_name['lastLink']._serialized_options = b'\030\001'
    _globals['_TMSHARDINFO'].fields_by_name['peerchain']._loaded_options = None
    _globals['_TMSHARDINFO'].fields_by_name['peerchain']._serialized_options = b'\030\001'
    _globals['_TMPROPOSESET'].fields_by_name['checkedSignature']._loaded_options = None
    _globals['_TMPROPOSESET'].fields_by_name['checkedSignature']._serialized_options = b'\030\001'
    _globals['_TMPROPOSESET'].fields_by_name['hops']._loaded_options = None
    _globals['_TMPROPOSESET'].fields_by_name['hops']._serialized_options = b'\030\001'
    _globals['_TMVALIDATION'].fields_by_name['checkedSignature']._loaded_options = None
    _globals['_TMVALIDATION'].fields_by_name['checkedSignature']._serialized_options = b'\030\001'
    _globals['_TMVALIDATION'].fields_by_name['hops']._loaded_options = None
    _globals['_TMVALIDATION'].fields_by_name['hops']._serialized_options = b'\030\001'
    _globals['_MESSAGETYPE']._serialized_start=3616
    _globals['_MESSAGETYPE']._serialized_end=4101
    _globals['_TRANSACTIONSTATUS']._serialized_start=4104
    _globals['_TRANSACTIONSTATUS']._serialized_end=4265
    _globals['_NODESTATUS']._serialized_start=4267
    _globals['_NODESTATUS']._serialized_end=4366
    _globals['_NODEEVENT']._serialized_start=4368
    _globals['_NODEEVENT']._serialized_end=4464
    _globals['_TXSETSTATUS']._serialized_start=4466
    _globals['_TXSETSTATUS']._serialized_end=4518
    _globals['_TMLEDGERINFOTYPE']._serialized_start=4520
    _globals['_TMLEDGERINFOTYPE']._serialized_end=4600
    _globals['_TMLEDGERTYPE']._serialized_start=4602
    _globals['_TMLEDGERTYPE']._serialized_end=4661
    _globals['_TMQUERYTYPE']._serialized_start=4663
    _globals['_TMQUERYTYPE']._serialized_end=4692
    _globals['_TMREPLYERROR']._serialized_start=4694
    _globals['_TMREPLYERROR']._serialized_end=4759
    _globals['_TMLEDGERMAPTYPE']._serialized_start=4761
    _globals['_TMLEDGERMAPTYPE']._serialized_end=4818
    _globals['_TMMANIFEST']._serialized_start=33
    _globals['_TMMANIFEST']._serialized_end=63
    _globals['_TMMANIFESTS']._serialized_start=65
    _globals['_TMMANIFESTS']._serialized_end=135
    _globals['_TMCLUSTERNODE']._serialized_start=137
    _globals['_TMCLUSTERNODE']._serialized_end=244
    _globals['_TMLOADSOURCE']._serialized_start=246
    _globals['_TMLOADSOURCE']._serialized_end=303
    _globals['_TMCLUSTER']._serialized_start=305
    _globals['_TMCLUSTER']._serialized_end=408
    _globals['_TMGETSHARDINFO']._serialized_start=410
    _globals['_TMGETSHARDINFO']._serialized_end=489
    _globals['_TMSHARDINFO']._serialized_start=492
    _globals['_TMSHARDINFO']._serialized_end=622
    _globals['_TMLINK']._serialized_start=624
    _globals['_TMLINK']._serialized_end=652
    _globals['_TMGETPEERSHARDINFO']._serialized_start=654
    _globals['_TMGETPEERSHARDINFO']._serialized_end=743
    _globals['_TMPEERSHARDINFO']._serialized_start=746
    _globals['_TMPEERSHARDINFO']._serialized_end=878
    _globals['_TMTRANSACTION']._serialized_start=881
    _globals['_TMTRANSACTION']._serialized_end=1009
    _globals['_TMSTATUSCHANGE']._serialized_start=1012
    _globals['_TMSTATUSCHANGE']._serialized_end=1231
    _globals['_TMPROPOSESET']._serialized_start=1234
    _globals['_TMPROPOSESET']._serialized_end=1477
    _globals['_TMHAVETRANSACTIONSET']._serialized_start=1479
    _globals['_TMHAVETRANSACTIONSET']._serialized_end=1554
    _globals['_TMVALIDATORLIST']._serialized_start=1556
    _globals['_TMVALIDATORLIST']._serialized_end=1641
    _globals['_VALIDATORBLOBINFO']._serialized_start=1643
    _globals['_VALIDATORBLOBINFO']._serialized_end=1713
    _globals['_TMVALIDATORLISTCOLLECTION']._serialized_start=1715
    _globals['_TMVALIDATORLISTCOLLECTION']._serialized_end=1821
    _globals['_TMVALIDATION']._serialized_start=1823
    _globals['_TMVALIDATION']._serialized_end=1905
    _globals['_TMENDPOINTS']._serialized_start=1908
    _globals['_TMENDPOINTS']._serialized_end=2050
    _globals['_TMENDPOINTS_TMENDPOINTV2']._serialized_start=1998
    _globals['_TMENDPOINTS_TMENDPOINTV2']._serialized_end=2044
    _globals['_TMINDEXEDOBJECT']._serialized_start=2052
    _globals['_TMINDEXEDOBJECT']._serialized_end=2147
    _globals['_TMGETOBJECTBYHASH']._serialized_start=2150
    _globals['_TMGETOBJECTBYHASH']._serialized_end=2469
    _globals['_TMGETOBJECTBYHASH_OBJECTTYPE']._serialized_start=2331
    _globals['_TMGETOBJECTBYHASH_OBJECTTYPE']._serialized_end=2469
    _globals['_TMLEDGERNODE']._serialized_start=2471
    _globals['_TMLEDGERNODE']._serialized_end=2519
    _globals['_TMGETLEDGER']._serialized_start=2522
    _globals['_TMGETLEDGER']._serialized_end=2758
    _globals['_TMLEDGERDATA']._serialized_start=2761
    _globals['_TMLEDGERDATA']._serialized_end=2957
    _globals['_TMPING']._serialized_start=2960
    _globals['_TMPING']._serialized_end=3093
    _globals['_TMPING_PINGTYPE']._serialized_start=3059
    _globals['_TMPING_PINGTYPE']._serialized_end=3093
    _globals['_TMSQUELCH']._serialized_start=3095
    _globals['_TMSQUELCH']._serialized_end=3173
    _globals['_TMPROOFPATHREQUEST']._serialized_start=3175
    _globals['_TMPROOFPATHREQUEST']._serialized_end=3269
    _globals['_TMPROOFPATHRESPONSE']._serialized_start=3272
    _globals['_TMPROOFPATHRESPONSE']._serialized_end=3442
    _globals['_TMREPLAYDELTAREQUEST']._serialized_start=3444
    _globals['_TMREPLAYDELTAREQUEST']._serialized_end=3486
    _globals['_TMREPLAYDELTARESPONSE']._serialized_start=3488
    _globals['_TMREPLAYDELTARESPONSE']._serialized_end=3613
# @@protoc_insertion_point(module_scope)