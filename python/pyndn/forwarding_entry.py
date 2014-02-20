#
# Copyright (C) 2014 Regents of the University of California.
# Author: Jeff Thompson <jefft0@remap.ucla.edu>
# See COPYING for copyright and distribution information.
#

"""
This module defines the ForwardingEntry class which holds an action and Name 
prefix and other fields for a forwarding entry.
"""

from pyndn.forwarding_flags import ForwardingFlags
from pyndn.name import Name
from pyndn.encoding import WireFormat
from pyndn.util import Blob

class ForwardingEntry(object):
    def __init__(self):
        self._action = None
        self._prefix = Name()
        self._faceId = None
        self._forwardingFlags = ForwardingFlags()
        self._freshnessPeriod = None
        
    def getAction(self):
        """
        Get the action string.
        
        :return: The action string, or None if not specified.
        :rtype: str
        """
        return self._action

    def getPrefix(self):
        """
        Get the name prefix.
        
        :return: The name prefix.
        :rtype: Name
        """
        return self._prefix
    
    def getFaceId(self):
        """
        Get the face ID, which is only meaningful if getAction() is 
        "prefixreg" or "unreg".
        
        :return: The face ID, or None if not specified.
        :rtype: int
        """
        return self._faceId
    
    def getForwardingFlags(self):
        """
        Get the ForwardingFlags object.
        
        :return: the ForwardingFlags object.
        :rtype: ForwardingFlags
        """
        return self._forwardingFlags
    
    def getFreshnessPeriod(self):
        """
        Get the freshness period.
        
        :return: The freshness period in milliseconds, or None if not specified.
        :rtype: float
        """
        return self._freshnessPeriod

    def setAction(self, action):
        """
        Set the action string.
        
        :param action: The new action string, or None for not specified.
        :type action: str
        """
        self._action = action
        
    def setFaceId(self, faceId):
        """
        Set the Face ID.
        
        :param faceId: The new face ID, or None for not specified.
        :type faceId: int
        """
        self._faceId = faceId
        
    def setForwardingFlags(self, forwardingFlags):
        """
        Set the ForwardingFlags object to a copy of forwardingFlags.  
        You can use getForwardingFlags() and change the existing 
        ForwardingFlags object.
        
        :param forwardingFlags: The new ForwardingFlace object.
        :type forwardingFlags: ForwardingFlags
        """
        self._forwardingFlags = (ForwardingFlags(forwardingFlags)
                                 if type(forwardingFlags) is ForwardingFlags
                                 else ForwardingFlags())
                                 
    def setFreshnessPeriod(self, freshnessPeriod):
        """
        Set the freshness period.
        
        :param freshnessPeriod: The freshness period in milliseconds, or None 
          for not specified.
        :type freshnessPeriod: float
        """
        self._freshnessPeriod = freshnessPeriod
    
    def wireEncode(self, wireFormat = WireFormat.getDefaultWireFormat()):
        """
        Encode this ForwardingEntry for a particular wire format.
        
        :param wireFormat: (optional) A WireFormat object used to encode this 
           ForwardingEntry. If omitted, use WireFormat.getDefaultWireFormat().
        :type wireFormat: A subclass of WireFormat.
        :return: The encoded buffer.
        :rtype: Blob
        """
        return wireFormat.encodeForwardingEntry(self)
    
    def wireDecode(self, input, wireFormat = WireFormat.getDefaultWireFormat()):
        """
        Decode the input using a particular wire format and update this 
        ForwardingEntry.
        
        :param input: The array with the bytes to decode.
        :type input: An array type with int elements
        :param wireFormat: (optional) A WireFormat object used to decode this 
           ForwardingEntry. If omitted, use WireFormat.getDefaultWireFormat().
        :type wireFormat: A subclass of WireFormat.
        """
        # If input is a blob, get its buf().
        decodeBuffer = input.buf() if isinstance(input, Blob) else input
        wireFormat.decodeForwardingEntry(self, decodeBuffer)