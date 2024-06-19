import time
from telethon import TelegramClient, errors

# Replace 'API_ID' and 'API_HASH' with your actual API ID and Hash
api_id = '22435521'
api_hash = 'c21b7141e3b89e0fa26267f855cfede1'

# Replace 'PHONE_NUMBER' with your phone number associated with Telegram
phone_number = '+3268540307'

# Message link to fetch content from
message_link = 'https://t.me/arsismm/12'

# List of channel IDs or usernames
channels = ['https://t.me/unseen_sus', 'https://t.me/Bhartiya_Group_9', 'https://t.me/SpaceX_Seller02', 'https://t.me/DOMSELLINGS', 'https://t.me/IndianSellersCrew', 'https://t.me/APSELLERS_06', 'https://t.me/haramysellers', 'https://t.me/selleropShoppingGroup', 't.me/heistbuyandsell', 'https://t.me/heistbuyandsell', 't.me/munnazkingdom3', 't.me/RAJPUTsellings3', 't.me/TYSON_seller_HUB', 't.me/heistbuyandselling4', 't.me/Bhartiya_Group_4', 'https://t.me/SpaceX_Seller03', 'https://t.me/InducedSelling', 'https://t.me/ATOMIC_STORE1', 'https://t.me/Bhartiya_Group_7', 'https://t.me/FAKKY_SELLERS', 'https://t.me/Jodselling', 'https://t.me/THEHEISTNETWORKGROUP', 'https://t.me/APSELLERS_14', 'https://t.me/CGSELLERS', 't.me/jodselling3', 't.me/MGMART21334', 't.me/SELLERS_Z0NE', 't.me/SELLING_CITY', 't.me/GodZ_Sellers7', 't.me/GodZ_Sellers6', 't.me/samXproofs', 't.me/TrustedSellers_everything', 't.me/ErrorSelling', 't.me/Shinobi_Sellings_2', 't.me/HiddenSellers_4', 't.me/THEAPSUPPORT', 't.me/berlinselling4', 't.me/PREMIUM_SELLING_DEALZ_4', 't.me/MadReSellers', 't.me/LOREM_SELLING', 't.me/SpaceX_Seller', 't.me/TheWizardSupport', 't.me/HiddenSellers_5', 't.me/ESCROW_SELLERZ_3', 't.me/united_sellers11', 't.me/selling_club', 't.me/ESCROWADDA1', 't.me/heistbuyandselling4', 't.me/HDSMM_SELLERS', 't.me/UNIQUE_SELLERS', 't.me/AlphaSellers4', 't.me/Bhartiya_Group_5', 't.me/jodselling2', 'https://t.me/PREMIUM_SELLING_DEALZ_5', 'https://t.me/escrowworlds', 'https://t.me/BeAsTSQuad_Selling', 't.me/wtbwtsaliannn', 'https://t.me/Warszawa022', 'https://t.me/Bhartiya_Group_7', 'https://t.me/SELLERS_Z0NE', 'https://t.me/Bhartiya_Group_7', 'https://t.me/gm2lmarket', 'https://t.me/IndianSellersCrew3', 'https://t.me/haramysellers', 'https://t.me/warszawaWtsWtb', 'https://t.me/wtbwtsaliannn', 'https://t.me/SELLERSUNIVERSE', 'https://t.me/MARIOSELLINGS', 'https://t.me/lpmsfsbeomgyu', 'https://t.me/PREMIUM_SELLING_DEALZ_4', 'https://t.me/Bhartiya_Group_9', 'https://t.me/APSELLERS_06', 'https://t.me/Bhartiya_Group_8', 'https://t.me/heistbuyandsell', 'https://t.me/Jodselling', 'https://t.me/escrowworlds', 'https://t.me/INDIANSELLING_HUB', 'https://t.me/SELLERS_ARMY', 'https://t.me/berlinselling4', 'https://t.me/Shinobi_Sellings_2', 'https://t.me/samXproofs', 'https://t.me/GodZ_Sellers7', 'https://t.me/TYSON_seller_HUB', 'https://t.me/premiumsellings', 'https://t.me/IndianSellersCrew', 'https://t.me/APSELLERS_012', 'https://t.me/Skull_support', 'https://t.me/empyrusWB', 'https://t.me/TheWizardSupport', 'https://t.me/InducedSelling', 'https://t.me/HiddenSellers_5', 'https://t.me/fors_ell2', 'https://t.me/heistbuyandselling6', 'https://t.me/APSELLERS_14', 'https://t.me/DOMSELLINGS', 'https://t.me/Infinite_sellers', 'https://t.me/selling_club', 'https://t.me/Sellingandbuyinghub', 'https://t.me/ESCROW_SELLERZ_3', 'https://t.me/indiansellerskingdom', 'https://t.me/ESCROWADDA1', 'https://t.me/THEHEISTNETWORKGROUP', 'https://t.me/united_sellers11', 'https://t.me/wheretosell', 'https://t.me/Bhartiya_Group_4', 'https://t.me/prosellertown_2', 'https://t.me/The_Official_Sellers', 'https://t.me/AlphaSellers4', 'https://t.me/BeAsTSQuad_Selling', 'https://t.me/prosellertown_5', 'https://t.me/SpaceX_Seller01', 'https://t.me/AP_OFFICIAL_SELLERS', 'https://t.me/SELLING_CITY', 'https://t.me/skull_sellings_3', 'https://t.me/RAJPUTsellings3', 'https://t.me/ErrorSelling','https://t.me/SELLINGHIDDEN', 'https://t.me/IndianSellers3', 'https://t.me/adsense_buy_and_sell', 'https://t.me/BuySell98u', 'https://t.me/premium_ac_selling', 'https://t.me/FANTASYSELLERS', 'https://t.me/telewts']

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Client Created")

    # Parse the link to get the channel ID and message ID
    parts = message_link.split('/')
    channel_username = parts[-2]
    message_id = int(parts[-1])

    try:
        # Retrieve the original message entity
        original_channel = await client.get_entity(channel_username)
        original_message = await client.get_messages(original_channel, ids=message_id)

        if not original_message:
            print("Failed to fetch the message content.")
            return
    except Exception as e:
        print(f'Failed to retrieve the original message: {e}')
        return
    
    while True:
        for channel in channels:
            try:
                # Retrieve the entity for the target channel
                target_channel = await client.get_entity(channel)
                # Forward the fetched message to the target channel
                await client.forward_messages(target_channel, original_message)
                print(f'Message forwarded to {channel}')
            except errors.rpcerrorlist.FloodWaitError as e:
                print(f'Flood wait error: need to wait {e.seconds} seconds')
                time.sleep(e.seconds)
            except errors.rpcerrorlist.ChatWriteForbiddenError:
                print(f'Cannot send message to {channel}: write access forbidden')
            except Exception as e:
                print(f'Failed to send message to {channel}: {e}')
            
            # Wait for 20 seconds before sending the next message
            time.sleep(0.1)

with client:
    client.loop.run_until_complete(main())
