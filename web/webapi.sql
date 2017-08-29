-- phpMyAdmin SQL Dump
-- version 4.0.9
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Erstellungszeit: 29. Aug 2017 um 11:37
-- Server Version: 5.5.33a-MariaDB
-- PHP-Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `webapi`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `votes`
--

CREATE TABLE IF NOT EXISTS `votes` (
  `id` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `cluster_id` int(11) NOT NULL,
  `yes` int(11) NOT NULL,
  `no` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `votes`
--

INSERT INTO `votes` (`id`, `name`, `cluster_id`, `yes`, `no`) VALUES
(15, 'Amazon SES', 503, 0, 1),
(106, 'Amazon RDS Relational Database Service', 503, 0, 1),
(143, 'Amazon SimpleDB', 503, 0, 1),
(155, 'Amazon Mechanical Turk', 503, 0, 1),
(285, 'Amazon EC2', 503, 0, 1),
(290, 'Amazon S3', 503, 0, 1),
(301, 'Amazon Product Advertising', 503, 0, 1),
(430, 'Sensebot', 503, 0, 1),
(432, 'Amazon CloudWatch', 503, 0, 1),
(440, 'ImageShack', 446, 1, 0),
(480, 'Amazon Queue Service', 503, 0, 1),
(519, 'BlankSlate', 259, 0, 1),
(559, 'Widgetbox', 35, 0, 1),
(561, 'Amazon Fulfillment Web Service', 503, 0, 1),
(564, 'NPR', 65, 0, 1),
(591, 'Bittrex', 402, 1, 0),
(609, 'LinkedIn People Search', 35, 1, 0),
(628, 'eRail.in Indian Railways', 65, 1, 0),
(731, 'Phanfare', 446, 1, 0),
(770, 'New York Times TimesPeople', 35, 1, 0),
(815, 'FreebieSMS', 289, 1, 0),
(865, 'Amazon SNS', 503, 0, 1),
(892, 'iRail', 65, 1, 0),
(919, 'EPA Watershed Summary', 65, 0, 1),
(920, 'EPA Station Catalog', 65, 0, 2),
(933, 'EyeEm', 446, 1, 0),
(941, 'ServiceNow', 291, 0, 3),
(949, 'Coderwall Profile', 35, 1, 0),
(1008, 'yfrog', 446, 1, 0),
(1035, 'A View From My Seat', 446, 0, 1),
(1050, 'Amazon Redshift', 503, 0, 1),
(1133, 'Amazon Elastic MapReduce', 503, 0, 1),
(1144, 'GoMoText SMS Gateway', 289, 0, 1),
(1181, 'IIG Alerts', 289, 0, 1),
(1184, 'BART', 65, 1, 0),
(1200, 'Yahoo Social Directory', 35, 1, 0),
(1244, 'Expono', 446, 1, 0),
(1849, 'Indian Rail', 65, 1, 0),
(1860, 'Macromeasures', 35, 0, 1),
(1895, 'PRP Services Private Limited Messaging', 289, 1, 0),
(2078, 'Minio', 503, 0, 1),
(2227, 'IbanFirst', 291, 0, 1),
(2230, 'Amazon Web Services Lambda', 503, 0, 1),
(2266, 'Amazon Web Services Lex', 503, 0, 1),
(2390, 'Eurobits Content Aggregation Service', 291, 0, 1),
(2511, 'MRT Singapore SMRT', 65, 1, 0),
(2531, 'Bitfinex Websocket', 402, 1, 0),
(2584, 'BlockCypher Analytics', 259, 0, 1),
(2590, 'Intis Telecom SMS', 289, 1, 0),
(2715, 'Amazon Web Services OpsWorks for Chef Automate', 503, 0, 1),
(2716, 'Amazon Web Services Pinpoint', 503, 0, 1),
(2721, 'Amazon Web Services AppStream', 503, 0, 1),
(2725, 'Amazon Web Services Health', 503, 0, 1),
(2726, 'Amazon Web Services CodeBuild', 503, 0, 1),
(2782, 'Amazon Alexa Smart Home Skills', 503, 0, 1),
(2808, 'Amazon Incentives', 503, 0, 1),
(2970, 'Salesforce.com Radian6', 35, 1, 0),
(3012, 'Zoom Connect SMS', 289, 1, 0),
(3013, 'Zoom Connect SMS Swagger', 289, 1, 0),
(3015, 'Makemoji', 503, 0, 1),
(3053, 'Block Explorer Web Socket', 259, 1, 0),
(3236, 'Urban Algorithms Geo Data', 35, 0, 1),
(3337, 'Apifaketory', 35, 0, 1),
(3633, 'LeakedSource', 35, 0, 1),
(3661, 'EtherScan Accounts', 259, 0, 1),
(3662, 'EtherScan Websockets', 259, 0, 1),
(3663, 'EtherScan Geth Proxy', 259, 2, 1),
(3664, 'EtherScan General Stats', 259, 0, 1),
(3665, 'EtherScan Event Logs', 259, 0, 1),
(3666, 'EtherScan Token Info', 259, 1, 0),
(3723, 'Berlin Public Transport REST', 65, 1, 0),
(3793, 'Skills Library', 35, 0, 1),
(4035, 'Atlas of Living Australia', 35, 0, 1),
(4186, 'allmysms HTTP', 289, 1, 0),
(4291, 'Bitcoin Chain', 259, 1, 0),
(4301, 'Amazon MWS', 503, 0, 1),
(4422, 'SNCF', 65, 1, 0),
(4509, 'RocketReach', 35, 1, 0),
(4702, 'London Tube', 65, 1, 0),
(4857, 'BlockCypher Metadata', 259, 0, 1),
(4858, 'BlockCypher Address', 259, 1, 0),
(4859, 'BlockCypher Asset', 259, 1, 0),
(4860, 'BlockCypher Wallet', 259, 1, 0),
(5233, 'Vaultoro Trading', 402, 1, 0),
(5270, 'LeadSift Consumers Insights', 35, 1, 0),
(5280, 'IAmReal Social Validation', 35, 1, 0),
(5310, 'Spiritual Networks', 35, 1, 0),
(5314, 'WaniKani', 35, 0, 1),
(5353, 'Blockchain Create Wallet', 259, 1, 0),
(5355, 'Blockchain Receive Payments', 259, 1, 0),
(5373, 'Blockchain Data', 259, 1, 0),
(5394, 'Amazon Gateway', 503, 0, 1),
(5546, 'Amazon WorkSpaces', 503, 0, 1),
(5547, 'Spectra Logic DS3', 503, 0, 1),
(5593, 'Cointrader.net', 402, 1, 0),
(6039, 'Connect Media Bulk SMS', 289, 1, 0),
(6119, 'Run The Red SMS', 289, 1, 0),
(6129, 'Twenty15Coin', 402, 2, 0),
(6248, 'DeftureSMS', 289, 1, 0),
(6313, 'Amazon Cloud Drive', 503, 0, 1),
(6330, 'Amazon Cloud Drive Account', 503, 0, 1),
(6331, 'Amazon Cloud Drive Nodes', 503, 0, 1),
(6332, 'Amazon Cloud Drive Changes', 503, 0, 1),
(6333, 'Amazon Cloud Drive Trash', 503, 0, 1),
(6371, 'KoKoMessaging', 289, 1, 0),
(6405, 'massenversand.de', 289, 1, 0),
(6410, 'Blockstrap', 259, 1, 0),
(6417, 'SpringEdge SMS', 289, 1, 0),
(6448, 'CoinCorner', 402, 1, 0),
(6504, 'Bitcore', 402, 1, 0),
(6542, 'Bitcoin.co.id', 402, 1, 0),
(6548, 'Open New York Transit Subway Entrance And Exit Data', 65, 1, 0),
(6588, 'Unofficial Ello', 35, 1, 0),
(6607, 'OKCoin', 402, 1, 0),
(6608, 'Huobi', 402, 1, 0),
(6609, 'BTCXIndia', 402, 1, 0),
(6610, 'igot', 402, 1, 0),
(6611, 'BTC Markets', 402, 1, 0),
(6612, 'Bitcoin.de', 402, 1, 0),
(6613, 'Bitso', 402, 1, 0),
(6614, 'LakeBTC', 402, 1, 0),
(6628, 'bx.in.th', 402, 1, 0),
(6643, 'Indian Railway', 65, 1, 0),
(6657, 'Qloudstat', 503, 0, 1),
(6669, 'Coinnext', 402, 1, 0),
(6708, 'LuxStack', 402, 2, 0),
(6713, 'Cozi', 446, 0, 1),
(6740, 'Comkort', 402, 2, 0),
(6762, 'Couchbase', 503, 0, 1),
(6780, 'Bitex.la Developer', 402, 2, 0),
(6791, 'Coingaia Trade', 402, 2, 0),
(6818, 'Self-service Bicycles', 65, 0, 1),
(6832, 'NetBulkSMS', 289, 1, 0),
(6866, 'bitNZ', 402, 2, 0),
(6970, 'Mintpal', 402, 1, 0),
(6971, 'Swisscex', 402, 1, 0),
(6992, 'Coinprism Colored Coins', 402, 1, 0),
(7020, 'Indacoin', 402, 1, 0),
(7021, 'CryptoCzar', 402, 1, 0),
(7022, 'CryptoAve', 402, 1, 0),
(7023, 'CoinSpot', 402, 1, 0),
(7024, 'Coinbroker.io', 402, 1, 0),
(7029, 'Express SMS', 289, 1, 0),
(7046, 'MyBitX', 402, 1, 0),
(7047, 'BitKonan', 402, 1, 0),
(7057, 'Atomic Trade', 402, 1, 0),
(7059, 'AllCoin', 402, 2, 0),
(7062, 'PlugChain', 259, 1, 0),
(7065, 'Toshi', 259, 1, 0),
(7074, 'Canadian Virtual Exchange', 402, 1, 0),
(7127, 'Kakao KakaoStory', 35, 1, 0),
(7143, 'APICoin BlockExplorer', 259, 1, 0),
(7175, 'Betarigs', 259, 0, 1),
(7186, 'Kakao KakaoTalk', 35, 1, 0),
(7284, 'BlisterPool P2Pool Donation', 259, 0, 1),
(7287, 'Chainz Developer', 259, 0, 1),
(7466, 'BTCDig', 259, 0, 1),
(7589, 'NYC Subway Data', 65, 1, 0),
(7600, 'BlockCypher', 259, 0, 1),
(7612, 'AGX', 402, 1, 0),
(7621, 'Stateful Web Primitives', 503, 0, 1),
(7627, 'Chain Block Chain', 259, 1, 1),
(7744, 'CrewRevu', 35, 0, 1),
(7796, 'RandomProfile', 35, 0, 1),
(7817, 'Your Fishing Report', 35, 1, 0),
(7823, 'Text2Africa', 289, 1, 0),
(7824, '24X7SMS', 289, 1, 0),
(7845, 'evamegsms', 289, 1, 0),
(7903, 'Earthquakes Canada Seismograph Stations', 65, 0, 1),
(7907, 'Wholesale SMS', 289, 1, 0),
(7937, 'SMSS South Africa', 289, 1, 0),
(8022, 'DogeChain', 259, 0, 1),
(8057, 'SlipSMS', 289, 1, 0),
(8062, 'Network Rail', 65, 1, 0),
(8079, 'The Ring Ring Company', 289, 1, 0),
(8130, 'YouSecond', 35, 1, 0),
(8134, 'SMS Ingenuity', 289, 1, 0),
(8136, 'SMS Central', 289, 1, 0),
(8185, 'Where the ISS at?', 65, 0, 1),
(8259, 'Jux', 446, 0, 1),
(8283, 'CNGnow', 65, 0, 1),
(8382, 'Hummingbird', 35, 0, 1),
(8540, 'Doximity', 35, 1, 0),
(8603, 'sendwithus', 503, 0, 1),
(8753, 'Bitx', 402, 1, 0),
(8976, 'TipTap Lab', 35, 0, 1),
(9010, 'GB Rail Info', 65, 1, 0),
(9011, 'MaxBTC', 259, 0, 1),
(9024, 'CoinMKT', 402, 1, 0),
(9146, 'Lake Sunapee Yacht Club Photo Album', 446, 0, 1),
(9209, 'Coderbits Profile', 35, 1, 0),
(9300, 'Block Chain Roulette', 259, 0, 1),
(9356, 'Litecoin Scout', 259, 0, 1),
(9489, 'Flipnote Hatena', 446, 1, 0),
(9490, 'Eligius', 259, 0, 1),
(9530, 'roondoo', 35, 1, 0),
(9652, '50BTC', 259, 0, 1),
(9821, 'navitia.io', 65, 1, 0),
(9881, 'CS Networks', 289, 1, 0),
(10047, 'Spendgate', 291, 0, 1),
(10101, 'Charlotte City Club Photo Album', 446, 0, 1),
(10106, 'IDlight', 35, 0, 1),
(10126, 'San Luis Obispo Country Club Photo Album', 446, 0, 1),
(10128, 'Tel-O-Fun Geo', 65, 0, 1),
(10130, 'The World Photo Album', 446, 1, 0),
(10134, 'Jonathan Club Photo Album', 446, 1, 0),
(10135, 'Glen Abbey Golf Club Photo Album', 446, 1, 0),
(10192, 'Pacific Links Hawaii Championship Photo Album', 446, 0, 1),
(10204, 'NA-ARC', 35, 0, 1),
(10361, 'National Rail Enquiries', 65, 1, 0),
(10379, 'SMSGateway.ca', 289, 1, 0),
(10385, 'FinancialForce Accounting', 291, 0, 1),
(10427, 'RunAlong', 35, 1, 0),
(10548, 'NJ Transit DepartureVision', 65, 1, 0),
(10574, 'Amazon Mobile App', 503, 0, 1),
(10584, 'OnlineCity NIMTA', 289, 1, 0),
(10613, 'Intacct Online Accounting', 291, 0, 1),
(10670, 'firmensms.at', 289, 1, 0),
(10737, 'FotoZap', 446, 1, 0),
(10741, 'NREL Alternative Fuel Stations', 65, 0, 1),
(10775, 'Irish Rail Realtime', 65, 1, 0),
(10787, 'Amazon CloudFront CDN', 503, 0, 1),
(10802, 'SC2Ranks', 35, 1, 0),
(10805, 'cortical.io Retina', 35, 0, 1),
(10951, '2sms', 289, 1, 0),
(10953, 'SlideSMS', 289, 1, 0),
(10954, 'Expert Web Worx', 289, 1, 0),
(11085, 'api4sms.net', 289, 1, 0),
(11162, 'IIAP Servicio Glosario', 503, 0, 1),
(11218, 'Amazon Glacier', 503, 0, 1),
(11228, 'Integrity Infotech Bulk SMS', 289, 1, 0),
(11237, 'Amazon ElastiCache', 503, 0, 1),
(11270, 'Gothia PayByBill', 291, 1, 1),
(11295, 'Myrrix', 503, 0, 1),
(11473, 'Mambu', 291, 0, 1),
(11548, 'SnapReplay', 446, 1, 0),
(11624, 'Avocado', 446, 0, 1),
(11664, 'Open Notify', 65, 0, 1),
(11670, 'TraitPerception', 35, 0, 1),
(11702, 'BTCMine', 259, 0, 1),
(11723, 'RouteSMS Javascript', 289, 1, 0),
(11805, 'RouteSMS', 289, 1, 0),
(12034, 'Heello', 446, 1, 0),
(12110, 'ShutterPro', 446, 1, 0),
(12261, 'Yahoo Wretch', 446, 1, 0),
(12350, 'Sohu Microblogging', 35, 1, 0),
(12487, 'Live Departure Boards', 65, 1, 0),
(12531, 'CTA Train Tracker', 65, 1, 0),
(12629, 'Zugmonitor', 65, 1, 0),
(12760, 'CommerceV3', 291, 0, 1),
(12790, 'Tastebuds.fm', 35, 0, 2),
(12843, 'Amazon Gift Cards', 503, 0, 1),
(12847, 'Snapjoy', 446, 9, 0),
(12945, 'Unofficial Fitocracy', 35, 1, 0),
(12957, 'TAgtider Trains', 65, 1, 0),
(13019, 'SavvisStation', 291, 0, 1),
(13185, 'EPA Project Catalog', 65, 0, 1),
(13186, 'EPA Station', 65, 0, 1),
(13274, 'IconCMO', 291, 0, 1),
(13452, 'SMStrade', 289, 1, 0),
(13523, 'deutschland', 35, 0, 1),
(13531, 'PSWinCom SMS Gateway', 289, 1, 0),
(13815, 'Oventus', 289, 1, 0),
(13841, 'Fliptop', 35, 1, 0),
(14022, 'Mnatives', 289, 1, 0),
(14125, 'BTBuckets', 35, 0, 1),
(14176, 'Dialogue Bulk SMS', 289, 1, 0),
(14379, 'Raveal', 35, 1, 0),
(14387, 'Shreeweb Bulk SMS', 289, 1, 0),
(14439, 'Human Information Project Data', 35, 1, 0),
(14582, 'Tube Updates', 65, 1, 0),
(14748, 'Geosion mobile SMS', 289, 1, 0),
(14797, 'FreebieSMS Auto Dialer', 289, 1, 0),
(14896, 'Profiles.im', 35, 1, 0),
(14990, 'Librarious', 503, 0, 1),
(14993, 'BuiltWith', 35, 0, 1),
(15150, 'Aerapay', 291, 1, 0),
(15166, 'Matrix SMS Gateway', 289, 1, 0),
(15175, 'Club Texting', 289, 1, 0),
(15368, 'Transport for London', 65, 1, 0),
(15584, 'TinyLoad', 503, 0, 1),
(15599, 'Amazon DevPay License Service', 503, 0, 1),
(15743, 'Dilogs', 35, 1, 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
