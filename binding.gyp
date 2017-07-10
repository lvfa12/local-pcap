{
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      'conditions': [
          [ 'OS=="win"', {
            'include_dirs': [
              'dependencies/winpcap/Include',
            ],
            'defines': [
              'WPCAP',
            ],
            'conditions': [
              [ 'target_arch=="ia32"', {
                'link_settings': {
                  'libraries': ['ws2_32.lib', '<(PRODUCT_DIR)/../../dependencies/winpcap/Lib/wpcap.lib'],
                },
              }, {
                'link_settings': {
                  'libraries': ['ws2_32.lib', '<(PRODUCT_DIR)/../../dependencies/winpcap/Lib/x64/wpcap.lib'],
                },
              }],
            ]
          }, {
            # POSIX
            'link_settings': {
              'libraries': ['-lpcap'],
            },
          }]
        ]
    }
  ]
}
