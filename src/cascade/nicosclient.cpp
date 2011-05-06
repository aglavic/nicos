// *****************************************************************************
// Module:
//   $Id$
//
// Author:
//   Tobias Weber <tweber@frm2.tum.de>
//
// NICOS-NG, the Networked Instrument Control System of the FRM-II
// Copyright (c) 2009-2011 by the NICOS-NG contributors (see AUTHORS)
//
// This program is free software; you can redistribute it and/or modify it under
// the terms of the GNU General Public License as published by the Free Software
// Foundation; either version 2 of the License, or (at your option) any later
// version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
// details.
//
// You should have received a copy of the GNU General Public License along with
// this program; if not, write to the Free Software Foundation, Inc.,
// 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
// *****************************************************************************

#include <iostream>

#include "nicosclient.h"
#include "helper.h"


NicosClient::NicosClient() : TcpClient(0, true), m_pad(0, true), m_tof(0, TOF_COMPRESSION_USEGLOBCONFIG, true)
{
	Config_TofLoader::Init();
}

NicosClient::~NicosClient()
{
	Config_TofLoader::Deinit();
}

const QByteArray& NicosClient::communicate(const char* pcMsg)
{
	cleanup<QMutex> _cleanup(m_mutex, &QMutex::unlock);	// unlock mutex at the end of the scope
	
	m_mutex.lock();
	if(!sendmsg(pcMsg))
		return m_byEmpty;
	
	const QByteArray& arr = recvmsg();
	return arr;
}

unsigned int NicosClient::counts(const QByteArray& arr, bool bPad)
{
	if(arr.size()<4) return 0;
	
	if(bPad)
	{
		m_pad.SetExternalMem((unsigned int*)(arr.data()+4));
		return m_pad.GetCounts();
	}
	else
	{
		m_tof.SetCompressionMethod(TOF_COMPRESSION_USEGLOBCONFIG);

		m_tof.SetExternalMem((unsigned int*)(arr.data()+4));
		unsigned int uiCnts = m_tof.GetCounts();
		m_tof.SetExternalMem(NULL);
		
		return uiCnts;
	}
}

unsigned int NicosClient::counts(const QByteArray& arr, bool bPad, int iStartX, int iEndX, int iStartY, int iEndY)
{
	if(arr.size()<4) 
		return 0;
	if(!IsSizeCorrect(arr, bPad))
		return 0;
	
	if(bPad)
	{
		m_pad.SetExternalMem((unsigned int*)(arr.data()+4));
		return m_pad.GetCounts(iStartX, iEndX, iStartY, iEndY);
	}
	else
	{
		m_tof.SetCompressionMethod(TOF_COMPRESSION_USEGLOBCONFIG);
		
		m_tof.SetExternalMem((unsigned int*)(arr.data()+4));
		unsigned int uiCnts = m_tof.GetCounts(iStartX, iEndX, iStartY, iEndY);
		m_tof.SetExternalMem(NULL);
		
		return uiCnts;
	}
}

bool NicosClient::IsSizeCorrect(const QByteArray& arr, bool bPad)
{
	bool bOk = true;
	if(bPad)
	{
		if(m_pad.GetPadSize() != arr.size()-4)
		{
			std::cerr << "NicosClient.counts: buffer size (" << arr.size()-4 << ") != expected PAD size (" << m_pad.GetPadSize() << ")" << std::endl;
			bOk = false;
		}
	}
	else
	{
		if(m_tof.GetTofSize() != arr.size()-4)
		{
			std::cerr << "NicosClient.counts: buffer size (" << arr.size()-4 << ") != expected TOF size (" << m_tof.GetTofSize() << ")" << std::endl;
			bOk = false;
		}
	}
	return bOk;
}
