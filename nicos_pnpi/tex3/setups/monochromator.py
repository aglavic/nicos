description = 'Monochromator movements'

tango_base = configdata('localconfig.tango_base')

m_x_conf = configdata('localconfig.M_X_CONF')
m_y_conf = configdata('localconfig.M_Y_CONF')
m_z_conf = configdata('localconfig.M_Z_CONF')
m_theta_conf = configdata('localconfig.M_THETA_CONF')
m_alpha_conf = configdata('localconfig.M_ALPHA_CONF')


devices = dict(
    m_x = device('nicos.devices.entangle.Motor',
                 description = m_x_conf['description'],
                 tangodevice = tango_base+'device/axis/m_x',
                 precision = m_x_conf['precision'],
                 lowlevel = m_x_conf['lowlevel'],
                 abslimits = m_x_conf['abslimits'],
                 speed = m_x_conf['speed'],
                 unit = m_x_conf['unit'],
                 ),
    m_y = device('nicos.devices.entangle.Motor',
                 description = m_y_conf['description'],
                 tangodevice = tango_base+'device/axis/m_y',
                 precision = m_y_conf['precision'],
                 lowlevel = m_y_conf['lowlevel'],
                 abslimits = m_y_conf['abslimits'],
                 speed = m_y_conf['speed'],
                 unit = m_y_conf['unit'],
                 ),
    m_z = device('nicos.devices.entangle.Motor',
                 description = m_z_conf['description'],
                 tangodevice = tango_base+'device/axis/m_z',
                 precision = m_z_conf['precision'],
                 lowlevel = m_z_conf['lowlevel'],
                 abslimits = m_z_conf['abslimits'],
                 speed = m_z_conf['speed'],
                 unit = m_z_conf['unit'],
                 ),


    m_theta = device('nicos.devices.entangle.Motor',
                     description = m_theta_conf['description'],
                     tangodevice = tango_base+'device/axis/m_theta',
                     precision = m_theta_conf['precision'],
                     lowlevel = m_theta_conf['lowlevel'],
                     abslimits = m_theta_conf['abslimits'],
                     speed = m_theta_conf['speed'],
                     unit = m_theta_conf['unit'],
                     ),
    m_alpha = device('nicos.devices.entangle.Motor',
                     description = m_alpha_conf['description'],
                     tangodevice = tango_base+'device/axis/m_alpha',
                     precision = m_alpha_conf['precision'],
                     lowlevel = m_alpha_conf['lowlevel'],
                     abslimits = m_alpha_conf['abslimits'],
                     speed = m_alpha_conf['speed'],
                     unit = m_alpha_conf['unit'],
                     ),
)
