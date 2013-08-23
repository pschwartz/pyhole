#   Copyright 2010-2011 Josh Kearney
#
#   Licensed under the Apachedexcept in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import log

from .irc.client import (Client,
                         active_commands,
                         active_keywords,
                         active_plugins)

from .irc.process import Process
